"""Parse Meta SDK codegen specs and generate FastMCP tool functions.

This module reads the JSON spec files from facebook-business-sdk-codegen
and generates Python async functions that wrap each API endpoint.

Usage:
    python -m meta_ads_mcp.generator
    # or
    from meta_ads_mcp.generator import generate_all
    generate_all(specs_dir, output_dir)
"""

import json
import re
from pathlib import Path
from typing import Any


# Which spec files to process and how to group them into modules
SPEC_MODULES: dict[str, list[str]] = {
    # --- Ads / Marketing (core) ---
    "accounts": ["AdAccount", "AdAccountCreationRequest"],
    "campaigns": ["Campaign"],
    "adsets": ["AdSet"],
    "ads": ["Ad"],
    "creatives": ["AdCreative", "AdVideo", "Canvas"],
    "audiences": ["CustomAudience"],
    "images": ["AdImage"],
    "rules": ["AdRule"],
    "pixels": [
        "AdsPixel", "OfflineConversionDataSet", "CustomConversion",
        "OfflineConversionDataSetUpload", "OffsiteSignalContainerBusinessObject",
        "OpenBridgeConfiguration", "EventSourceGroup",
    ],
    "ad_studies": ["AdStudy", "AdStudyObjective", "AdStudyCell"],
    "ad_labels": ["AdLabel"],
    "ad_async": ["AdAsyncRequest", "AdAsyncRequestSet", "AdReportRun"],
    "ad_monetization": ["AdMonetizationProperty", "AdsConversionGoal", "AdsValueAdjustmentRuleCollection"],
    # --- Instagram ---
    "instagram": ["IGUser", "IGMedia", "IGComment", "IGUpcomingEvent", "ShadowIGHashtag"],
    "instagram_only_api": ["IGUserForIGOnlyAPI", "IGMediaForIGOnlyAPI"],
    "instagram_business": ["InstagramBusinessAsset", "InstagramUser", "IGUserExportForCAM"],
    # --- Pages / Content ---
    "pages": ["Page", "PagePost", "PageCallToAction", "PagePostExperiment", "PageUserMessageThreadLabel"],
    "content": ["Post", "Comment", "Photo", "Album", "LiveVideo", "Event", "Stories", "Link", "Status"],
    "media": ["MediaTitle", "MediaFingerprint", "VideoList", "VideoPoll", "VideoCopyright", "AudioCopyright", "ImageCopyright", "RTBDynamicPost"],
    # --- Business ---
    "business": [
        "Business", "BusinessUser", "BusinessAssetGroup", "SystemUser",
        "BusinessRoleRequest", "BusinessAgreement", "BusinessAssetSharingAgreement",
    ],
    "extended_credit": ["ExtendedCredit", "ExtendedCreditInvoiceGroup", "ExtendedCreditAllocationConfig"],
    # --- Product Catalog ---
    "catalog": [
        "ProductCatalog", "ProductFeed", "ProductSet", "ProductItem", "ProductGroup",
        "ProductFeedRule", "ProductFeedUpload", "ProductFeedUploadError",
        "StoreCatalogSettings", "OfflineProductItem",
    ],
    # --- Commerce ---
    "commerce": ["CommerceOrder", "CommerceMerchantSettings", "CommerceOrderTransactionDetail"],
    # --- Lead Gen ---
    "lead_gen": ["LeadgenForm", "Lead"],
    # --- WhatsApp Business ---
    "whatsapp": ["WhatsAppBusinessAccount", "WhatsAppBusinessPreVerifiedPhoneNumber", "WhatsAppBusinessProfile"],
    # --- Verticals (Travel / Auto / Real Estate) ---
    "verticals": ["Hotel", "HotelRoom", "Flight", "Destination", "Vehicle", "VehicleOffer", "AutomotiveModel", "HomeListing", "HighDemandPeriod", "TransactableItem", "LocalServiceBusiness"],
    # --- Messenger ---
    "messenger": ["MessengerAdsPartialAutomatedStepList", "MessengerBusinessTemplate", "Persona", "UnifiedThread"],
    # --- Other ---
    "applications": ["Application", "AppRequest"],
    "users": ["User", "Profile", "LifeEvent", "WorkSkill"],
    "groups": ["Group"],
    "publisher_block_lists": ["PublisherBlockList", "ContentBlockList"],
    "fundraiser": ["FundraiserPersonToCharity"],
    "cpas": ["CPASBusinessSetupConfig", "CPASLsbImageBank"],
    "payments": ["PaymentEnginePayment", "OmegaCustomerTrx"],
    "misc": ["URL", "PrivateLiftStudyInstance", "BizInboxOffsiteEmailAccount"],
}

# Endpoint naming: '#get' -> get_{node}, '#update' -> update_{node}, etc.
SELF_METHODS = {"#get": "get", "#update": "update", "#delete": "delete"}

# Skip these edges (internal, deprecated, or not useful for ads management)
SKIP_EDGES = {
    "activities",
    "adlabels",
    "trackingtag",
    "adrules_governed",
    "userpermissions",
}

# Python keywords/builtins that can't be used as parameter names (PEP 8: add trailing _)
import keyword as _keyword

PYTHON_RESERVED = set(_keyword.kwlist) | {
    "bytes", "filter", "object", "type", "zip", "id", "input", "format", "hash", "list", "map", "set",
}


def _safe_param_name(name: str) -> str:
    """Append underscore to Python reserved words (PEP 8 convention)."""
    return f"{name}_" if name in PYTHON_RESERVED else name

# Type mapping from Meta spec types to Python types
TYPE_MAP = {
    "string": "str",
    "int": "int",
    "unsigned int": "int",
    "float": "float",
    "bool": "bool",
    "datetime": "str",
    "Object": "str",
    "map": "str",
    "file": "str",
}


def _snake_case(name: str) -> str:
    """Convert CamelCase or mixed to snake_case.

    Args:
        name: CamelCase string like "AdAccount" or "CustomAudience".

    Returns:
        snake_case string like "ad_account" or "custom_audience".
    """
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    s = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s)
    return s.lower().replace(" ", "_").replace("-", "_")


def _python_type(spec_type: str) -> str:
    """Convert a Meta spec type to Python type annotation.

    Args:
        spec_type: Type string from the spec (e.g. "string", "int", "list<AdLabel>").

    Returns:
        Python type string (e.g. "str", "int").
    """
    if spec_type in TYPE_MAP:
        return TYPE_MAP[spec_type]
    if spec_type.startswith("list<"):
        return "str"  # Lists passed as JSON strings
    if "_enum_" in spec_type.lower():
        return "str"  # Enum values are strings
    return "str"  # Default to string


def _load_spec(specs_dir: Path, name: str) -> dict[str, Any]:
    """Load a spec JSON file.

    Args:
        specs_dir: Path to the specs/ directory.
        name: Spec name (e.g. "Campaign") — without .json extension.

    Returns:
        Parsed spec dict.

    Raises:
        FileNotFoundError: If the spec file does not exist.
    """
    path = specs_dir / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(f"Spec not found: {path}")
    with open(path) as f:
        return json.load(f)


def _load_enums(specs_dir: Path) -> dict[str, list[str]]:
    """Load enum definitions from enum_types.json.

    Args:
        specs_dir: Path to the specs/ directory.

    Returns:
        Dict mapping enum name to list of valid values.
    """
    path = specs_dir / "enum_types.json"
    if not path.exists():
        return {}
    with open(path) as f:
        data = json.load(f)
    # enum_types.json is a list of {name, node, field_or_param, values}
    if isinstance(data, list):
        return {e["name"]: e["values"] for e in data if "name" in e and "values" in e}
    return data


def _generate_fields_constant(spec_name: str, fields: list[dict]) -> str:
    """Generate a FIELDS constant listing all readable fields.

    Args:
        spec_name: Name of the spec (e.g. "Campaign").
        fields: List of field dicts from the spec.

    Returns:
        Python code defining a list constant of field names.
    """
    field_names = sorted(f["name"] for f in fields if f.get("name"))
    const_name = f"{_snake_case(spec_name).upper()}_FIELDS"
    fields_str = json.dumps(field_names, indent=4)
    return f"{const_name} = {fields_str}\n"


def _generate_function(
    spec_name: str,
    api: dict[str, Any],
    enums: dict[str, list[str]],
    node_snake: str,
    spec_fields: list[str] | None = None,
) -> str:
    """Generate a single async tool function from an API spec entry.

    Args:
        spec_name: Name of the spec (e.g. "Campaign").
        api: Single API entry from the spec's "apis" array.
        enums: Enum definitions for docstring hints.
        node_snake: snake_case version of the spec name.
        spec_fields: List of available field names for this spec (for GET docstrings).

    Returns:
        Python code for the async function.
    """
    endpoint = api.get("endpoint") or api.get("name", "")
    method = api["method"]
    params = api.get("params", [])

    # Determine function name and path template
    if endpoint in SELF_METHODS:
        action = SELF_METHODS[endpoint]
        func_name = f"{action}_{node_snake}"
        path_template = f"{{{node_snake}_id}}"
        id_param_name = f"{node_snake}_id"
    else:
        edge_snake = _snake_case(endpoint)
        if method == "POST":
            if endpoint == "copies":
                func_name = f"copy_{node_snake}"
                path_template = f"{{{node_snake}_id}}/{endpoint}"
                id_param_name = f"{node_snake}_id"
            else:
                func_name = f"create_{node_snake}_{edge_snake}"
                if spec_name == "AdAccount":
                    path_template = f"act_{{account_id}}/{endpoint}"
                    id_param_name = "account_id"
                else:
                    path_template = f"{{{node_snake}_id}}/{endpoint}"
                    id_param_name = f"{node_snake}_id"
        elif method == "GET":
            func_name = f"get_{node_snake}_{edge_snake}"
            path_template = f"{{{node_snake}_id}}/{endpoint}"
            id_param_name = f"{node_snake}_id"
        elif method == "DELETE":
            func_name = f"delete_{node_snake}_{edge_snake}"
            path_template = f"{{{node_snake}_id}}/{endpoint}"
            id_param_name = f"{node_snake}_id"
        else:
            func_name = f"{method.lower()}_{node_snake}_{edge_snake}"
            path_template = f"{{{node_snake}_id}}/{endpoint}"
            id_param_name = f"{node_snake}_id"

    # Build parameter list
    func_params = [f"{id_param_name}: str"]
    optional_params = []
    param_docs = [f"        {id_param_name}: The ID of the {spec_name} object."]

    # For GET endpoints, add a 'fields' parameter if not already in params
    has_fields_param = any(p["name"] == "fields" for p in params)
    if method == "GET" and not has_fields_param:
        optional_params.append("fields: Optional[str] = None")
        if spec_fields and endpoint in SELF_METHODS:
            fields_hint = f" Available: {', '.join(spec_fields)}"
            param_docs.append(f"        fields: Comma-separated list of fields to return.{fields_hint}")
        else:
            param_docs.append("        fields: Comma-separated list of fields to return.")

    # Track seen param names to avoid duplicates (id_param_name + fields already added)
    seen_params = {id_param_name}
    if method == "GET" and not has_fields_param:
        seen_params.add("fields")

    for p in params:
        pname = p["name"]

        # Skip duplicate params and Python keywords
        if pname in seen_params:
            continue
        seen_params.add(pname)

        safe_name = _safe_param_name(pname)
        ptype = _python_type(p.get("type", "string"))
        required = p.get("required", False)

        # Resolve enum values for docstring — show ALL values so agent knows what's available
        enum_hint = ""
        ptype_raw = p.get("type", "")
        enum_name = ptype_raw
        # Extract enum name from list<enum_name> wrapper
        if ptype_raw.startswith("list<") and ptype_raw.endswith(">"):
            enum_name = ptype_raw[5:-1]
        if "_enum_" in enum_name.lower():
            enum_values = enums.get(enum_name, [])
            if not enum_values:
                # Try the full type including list<> wrapper
                enum_values = enums.get(ptype_raw, [])
            if enum_values:
                enum_hint = f" Values: {', '.join(enum_values)}"

        if required:
            func_params.append(f"{safe_name}: {ptype}")
            param_docs.append(f"        {safe_name}: Required.{enum_hint}")
        else:
            optional_params.append(f"{safe_name}: Optional[{ptype}] = None")
            param_docs.append(f"        {safe_name}: Optional.{enum_hint}")

    all_params = func_params + optional_params

    # Build function body
    body_lines = []
    body_lines.append("    params = {}")

    if method == "GET":
        body_lines.append('    params["fields"] = fields or "id,name"')

    for p in params:
        pname = p["name"]
        safe_name = _safe_param_name(pname)
        if p.get("required", False):
            body_lines.append(f'    params["{pname}"] = {safe_name}')
        else:
            body_lines.append(f"    if {safe_name} is not None:")
            body_lines.append(f'        params["{pname}"] = {safe_name}')

    # API call
    path_code = f'f"{path_template}"'
    if method == "GET":
        body_lines.append(f"    result = await get_client().get({path_code}, params=params)")
    elif method == "POST":
        body_lines.append(f"    result = await get_client().post({path_code}, data=params)")
    elif method == "DELETE":
        body_lines.append(f"    result = await get_client().delete({path_code})")

    body_lines.append("    return json.dumps(result, indent=2)")

    # Assemble function
    all_params_str = ", ".join(all_params)
    if len(all_params_str) > 80:
        params_formatted = ",\n    ".join(all_params)
        signature = f"async def {func_name}(\n    {params_formatted},\n) -> str:"
    else:
        signature = f"async def {func_name}({all_params_str}) -> str:"

    docstring_lines = [
        f'    """{method} /{endpoint} on {spec_name}.',
        "",
        "    Args:",
    ] + param_docs + [
        '    """',
    ]

    func_code = "\n".join([signature] + docstring_lines + body_lines)
    return func_code


def generate_module(
    specs_dir: Path,
    spec_names: list[str],
    module_name: str,
    enums: dict[str, list[str]],
) -> str:
    """Generate a complete tool module from one or more spec files.

    Args:
        specs_dir: Path to the specs/ directory.
        spec_names: List of spec names to include in this module.
        module_name: Name for the generated module (e.g. "campaigns").
        enums: Enum definitions for docstring hints.

    Returns:
        Complete Python module source code.
    """
    lines = [
        f'"""Auto-generated Meta Marketing API tools — {module_name}."""',
        "",
        "import json",
        "from typing import Optional",
        "",
        "from meta_ads_mcp.client import get_client",
        "",
    ]

    for spec_name in spec_names:
        spec = _load_spec(specs_dir, spec_name)
        node_snake = _snake_case(spec_name)

        # Generate FIELDS constant
        fields = spec.get("fields", [])
        field_names = sorted(f["name"] for f in fields if f.get("name")) if fields else []
        if fields:
            lines.append(_generate_fields_constant(spec_name, fields))
            lines.append("")

        # Generate functions from APIs
        apis = spec.get("apis", [])
        for api in apis:
            edge = api.get("endpoint") or api.get("name", "")
            if edge in SKIP_EDGES:
                continue

            try:
                func_code = _generate_function(spec_name, api, enums, node_snake, spec_fields=field_names)
                lines.append(func_code)
                lines.append("")
                lines.append("")
            except Exception as e:
                lines.append(f"# SKIPPED: {edge} — {e}")
                lines.append("")

    return "\n".join(lines)


def generate_all(specs_dir: Path, output_dir: Path):
    """Generate all tool modules from the vendored specs.

    Args:
        specs_dir: Path to the specs/ directory.
        output_dir: Path to write generated tool modules (e.g. src/meta_ads_mcp/tools/).
    """
    enums = _load_enums(specs_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate __init__.py
    init_lines = ['"""Auto-generated Meta Marketing API tools."""', ""]

    total_functions = 0
    for module_name, spec_names in SPEC_MODULES.items():
        if not spec_names:
            continue

        module_code = generate_module(specs_dir, spec_names, module_name, enums)
        module_path = output_dir / f"{module_name}.py"
        module_path.write_text(module_code)

        # Count functions
        func_count = module_code.count("async def ")
        total_functions += func_count
        print(f"  {module_name}.py — {func_count} tools from {', '.join(spec_names)}")

        init_lines.append(f"from meta_ads_mcp.tools.{module_name} import *  # noqa: F403")

    # Write __init__.py
    (output_dir / "__init__.py").write_text("\n".join(init_lines) + "\n")

    print(f"\nTotal: {total_functions} tool functions generated across {len(SPEC_MODULES)} modules")


if __name__ == "__main__":
    root = Path(__file__).parent
    if root.name == "meta_ads_mcp":
        root = root.parent.parent
    generate_all(root / "specs", root / "src" / "meta_ads_mcp" / "tools")
