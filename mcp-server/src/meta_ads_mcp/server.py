"""meta-ads-mcp-codemode: Meta Marketing API via FastMCP Code Mode.

Auto-generated tools from facebook-business-sdk-codegen specs.
Agent sees 3 meta-tools: search, get_schema, execute.

WARNING: Connecting AI agents to Meta ad accounts carries risk of permanent
account ban. See README for required safety setup (App Review, System User
tokens, rate limit configuration).
"""

import importlib
import inspect
import logging
import os
import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastmcp import FastMCP
from fastmcp.experimental.transforms.code_mode import CodeMode, MontySandboxProvider

from meta_ads_mcp.client import get_client, close_client
from meta_ads_mcp.token_info import validate_token, log_token_warnings

# Manual tool modules
from meta_ads_mcp.tools.targeting import (
    search_targeting,
    get_broad_targeting_categories,
    get_targeting_sentence_lines,
)
from meta_ads_mcp.tools.generic import meta_api_call
from meta_ads_mcp.tools.status import rate_limit_status
from meta_ads_mcp.apps.instagram_dashboard import instagram_dashboard

logger = logging.getLogger("meta_ads_mcp")

# Write operations require explicit opt-in via env var
WRITE_MODE = os.environ.get("META_ADS_WRITE_MODE", "").lower() in ("true", "1", "yes")

# Modules that contain write operations (POST/DELETE endpoints)
_WRITE_INDICATORS = {"create_", "update_", "delete_", "remove_", "archive_"}

_SAFETY_WARNING = """
===================================================================
  META ADS MCP — SAFETY WARNING
===================================================================
  Connecting AI agents to Meta ad accounts can trigger permanent
  account bans with NO appeal process. This is actively happening
  as of March 2026.

  REQUIRED SETUP (see README):
  1. Create a Meta App and pass App Review
  2. Use System User tokens (not personal tokens)
  3. Apply for Advanced Access (Standard tier)
  4. Set META_APP_SECRET for appsecret_proof

  CURRENT MODE: {mode}
  Write operations are {write_status}.
===================================================================
"""


def _is_write_tool(func_name: str) -> bool:
    """Check if a tool function name indicates a write operation."""
    return any(func_name.startswith(prefix) for prefix in _WRITE_INDICATORS)


@asynccontextmanager
async def _app_lifespan(server):
    """Initialize shared MetaClient on startup, validate token, close on shutdown."""
    client = get_client()
    logger.info("Shared MetaClient initialized (single rate limiter + connection pool)")

    # Validate token on startup — detect type, permissions, expiration
    try:
        token_info = await validate_token(client)
        warnings = log_token_warnings(token_info, write_mode=WRITE_MODE)

        if not token_info.is_valid:
            print(
                f"\n  TOKEN ERROR: {token_info.error_message}\n"
                f"  The server will start but API calls will fail.\n",
                file=sys.stderr,
            )
        elif token_info.is_expired:
            print(
                "\n  TOKEN EXPIRED: Generate a new token.\n"
                "  System User tokens (Business Manager) are recommended.\n",
                file=sys.stderr,
            )
        elif warnings:
            for w in warnings:
                print(f"  WARNING: {w}", file=sys.stderr)

        if token_info.is_valid and not token_info.is_expired:
            tier = "System User" if token_info.is_system_user else "Personal"
            exp = "never" if token_info.never_expires else f"{token_info.expires_in_days:.0f} days"
            print(
                f"  Token: {tier} | Expires: {exp} | "
                f"Scopes: {', '.join(token_info.scopes) or 'unknown'}",
                file=sys.stderr,
            )

    except Exception as e:
        logger.warning("Token validation failed (server will still start): %s", e)

    try:
        yield {}
    finally:
        await close_client()
        logger.info("Shared MetaClient closed")


mcp = FastMCP(
    "meta-ads",
    lifespan=_app_lifespan,
    instructions=(
        "Meta Marketing API v25.0 MCP server with Code Mode. "
        "230+ tools auto-generated from Meta's official SDK specs. "
        "Use search to discover tools, get_schema for parameter details, "
        "then execute Python code using await call_tool(name, {params}). "
        "All tools return JSON strings. Parse with json.loads() if needed. "
        "Auth is handled automatically — never pass access_token as a parameter. "
        "v25.0 note: Advantage+ shopping/app campaigns are blocked — use Advantage+ campaigns structure. "
        "SAFETY: This server enforces rate limits per Meta's official guidelines. "
        "Write operations (create/update/delete) require META_ADS_WRITE_MODE=true. "
        "Monitor rate limit usage via the rate_limit_status tool."
    ),
)


def _register_generated_tools():
    """Discover and register all auto-generated tool functions from the tools/ directory.

    Scans src/meta_ads_mcp/tools/ for Python modules (excluding manual ones),
    imports each module, and registers all async functions as MCP tools.

    When WRITE_MODE is disabled, write tools (create_*, update_*, delete_*) are skipped.
    """
    tools_dir = Path(__file__).parent / "tools"
    skip_modules = {"__init__", "targeting", "generic", "status"}  # Manual modules registered separately

    registered = 0
    skipped_write = 0

    for module_path in sorted(tools_dir.glob("*.py")):
        module_name = module_path.stem
        if module_name in skip_modules:
            continue

        module = importlib.import_module(f"meta_ads_mcp.tools.{module_name}")
        for name, obj in inspect.getmembers(module, inspect.isfunction):
            if inspect.iscoroutinefunction(obj) and not name.startswith("_"):
                if not WRITE_MODE and _is_write_tool(name):
                    skipped_write += 1
                    continue
                mcp.tool(obj)
                registered += 1

    logger.info("Registered %d tools (%d write tools skipped)", registered, skipped_write)


# Register auto-generated tools
_register_generated_tools()

# Register manual tools
for tool_fn in [
    search_targeting,
    get_broad_targeting_categories,
    get_targeting_sentence_lines,
    meta_api_call,
    rate_limit_status,
]:
    mcp.tool(tool_fn)

# Register App tools (interactive dashboards — bypass Code Mode)
mcp.tool(instagram_dashboard, app=True)

# Apply Code Mode transform — agent sees 3 meta-tools: search, get_schema, execute
sandbox = MontySandboxProvider(
    limits={"max_duration_secs": 30, "max_memory": 100_000_000},
)
mcp.add_transform(CodeMode(sandbox_provider=sandbox))


def main():
    """Entry point for the meta-ads-mcp CLI command."""
    mode = "READ-WRITE" if WRITE_MODE else "READ-ONLY"
    write_status = "ENABLED (META_ADS_WRITE_MODE=true)" if WRITE_MODE else "DISABLED (default — safe mode)"

    print(_SAFETY_WARNING.format(mode=mode, write_status=write_status), file=sys.stderr)

    if not os.environ.get("META_ACCESS_TOKEN"):
        print("ERROR: META_ACCESS_TOKEN environment variable is required.", file=sys.stderr)
        sys.exit(1)

    if not os.environ.get("META_APP_SECRET"):
        print(
            "WARNING: META_APP_SECRET not set. appsecret_proof will not be sent. "
            "This is strongly recommended for production use.",
            file=sys.stderr,
        )

    mcp.run()


if __name__ == "__main__":
    main()
