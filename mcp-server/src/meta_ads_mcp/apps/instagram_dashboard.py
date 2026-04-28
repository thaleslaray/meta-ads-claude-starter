"""Instagram Analytics Dashboard — Prefab App PoC.

Fetches real data from Meta Graph API and renders an interactive dashboard
with charts and KPI cards inside the MCP client conversation.
"""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from prefab_ui.app import PrefabApp
from prefab_ui.components import (
    Badge,
    Column,
    Heading,
    Row,
    Separator,
    Tabs,
    Tab,
    Text,
)
from prefab_ui.components.charts import BarChart, ChartSeries
from prefab_ui.components.dashboard import Dashboard, DashboardItem
from prefab_ui.components.metric import Metric
from prefab_ui.components.data_table import DataTable, DataTableColumn

from meta_ads_mcp.client import MetaClient


async def _fetch_ig_data(ig_user_id: str) -> dict:
    """Fetch posts, insights, and profile data from Instagram Graph API."""
    client = MetaClient()
    try:
        # Get recent media
        media = await client.get_all_pages(
            f"{ig_user_id}/media",
            params={"fields": "id,caption,timestamp,media_type,media_product_type,like_count,comments_count,permalink"},
        )

        # Get insights per post (reach, follows, views)
        posts_data = []
        for post in media[:25]:  # Last 25 posts
            media_type = post.get("media_product_type", "FEED")
            if media_type == "REELS":
                metrics = "reach,views,saved,shares,comments,likes,follows"
            else:
                metrics = "reach,views,saved,shares,follows,profile_visits,total_interactions"

            try:
                insights = await client.get(
                    f"{post['id']}/insights",
                    params={"metric": metrics},
                )
                insight_map = {}
                for item in insights.get("data", []):
                    val = item.get("values", [{}])[0].get("value", 0)
                    insight_map[item["name"]] = val
            except Exception:
                insight_map = {}

            caption = post.get("caption", "")[:60]
            ts = post.get("timestamp", "")
            posts_data.append({
                "id": post["id"],
                "caption": caption,
                "timestamp": ts,
                "media_type": media_type,
                "like_count": post.get("like_count", 0),
                "comments_count": post.get("comments_count", 0),
                "reach": insight_map.get("reach", 0),
                "views": insight_map.get("views", 0),
                "follows": insight_map.get("follows", 0),
                "saves": insight_map.get("saved", 0),
                "shares": insight_map.get("shares", 0),
                "profile_visits": insight_map.get("profile_visits", 0),
            })

        # Get follower count
        try:
            profile = await client.get(
                ig_user_id,
                params={"fields": "username,followers_count,media_count,name"},
            )
        except Exception:
            profile = {}

        return {"posts": posts_data, "profile": profile}
    finally:
        await client.close()


def _build_dashboard(data: dict) -> PrefabApp:
    """Build a Prefab dashboard from the fetched data."""
    posts = data["posts"]
    profile = data["profile"]

    username = profile.get("username", "unknown")
    followers = profile.get("followers_count", 0)
    total_posts = profile.get("media_count", 0)

    # KPIs
    total_reach = sum(p["reach"] for p in posts)
    total_follows = sum(p["follows"] for p in posts)
    total_saves = sum(p["saves"] for p in posts)
    total_shares = sum(p["shares"] for p in posts)
    avg_engagement = 0
    if followers > 0:
        total_interactions = sum(p["like_count"] + p["comments_count"] + p["saves"] + p["shares"] for p in posts)
        avg_engagement = round((total_interactions / len(posts) / followers) * 100, 2) if posts else 0

    # Charts data: reach per post
    reach_data = []
    for i, p in enumerate(reversed(posts)):
        label = p["caption"][:25] or f"Post {i+1}"
        reach_data.append({"post": label, "reach": p["reach"], "follows": p["follows"]})

    # Best hour analysis
    hour_stats = defaultdict(lambda: {"reach": 0, "count": 0, "follows": 0})
    for p in posts:
        ts = p.get("timestamp", "")
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                hour = dt.hour
                hour_stats[hour]["reach"] += p["reach"]
                hour_stats[hour]["count"] += 1
                hour_stats[hour]["follows"] += p["follows"]
            except Exception:
                pass

    hour_data = []
    for h in sorted(hour_stats.keys()):
        s = hour_stats[h]
        avg_reach = round(s["reach"] / s["count"]) if s["count"] > 0 else 0
        hour_data.append({
            "hour": f"{h:02d}:00 UTC",
            "avg_reach": avg_reach,
            "posts": s["count"],
            "follows": s["follows"],
        })

    # Top posts table
    top_posts = sorted(posts, key=lambda p: p["follows"], reverse=True)[:10]
    table_data = []
    for p in top_posts:
        table_data.append({
            "caption": p["caption"][:40] or "(sem legenda)",
            "type": p["media_type"],
            "reach": f"{p['reach']:,}",
            "follows": p["follows"],
            "saves": p["saves"],
            "shares": p["shares"],
        })

    # Build the UI
    with Column(gap=6, cssClass="p-6 max-w-4xl mx-auto") as view:
        Heading(f"Instagram Analytics — @{username}", level=1)
        Text(f"{followers:,} followers · {total_posts} posts · últimos {len(posts)} posts analisados")
        Separator()

        # KPI row
        with Row(gap=4):
            Metric(label="Alcance Total", value=f"{total_reach:,}")
            Metric(label="Seguidores Ganhos", value=str(total_follows))
            Metric(label="Saves", value=str(total_saves))
            Metric(label="Eng. Médio", value=f"{avg_engagement}%")

        Separator()

        with Tabs():
            with Tab(title="Alcance por Post"):
                BarChart(
                    data=reach_data,
                    series=[ChartSeries(dataKey="reach", label="Reach")],
                    xAxis="post",
                    height=350,
                )

            with Tab(title="Follows por Post"):
                BarChart(
                    data=reach_data,
                    series=[ChartSeries(dataKey="follows", label="Follows")],
                    xAxis="post",
                    height=350,
                )

            with Tab(title="Melhor Horário"):
                BarChart(
                    data=hour_data,
                    series=[
                        ChartSeries(dataKey="avg_reach", label="Reach Médio"),
                        ChartSeries(dataKey="follows", label="Follows"),
                    ],
                    xAxis="hour",
                    height=350,
                    showLegend=True,
                )

            with Tab(title="Top Posts"):
                DataTable(
                    rows=table_data,
                    columns=[
                        DataTableColumn(key="caption", header="Post", sortable=True),
                        DataTableColumn(key="type", header="Tipo"),
                        DataTableColumn(key="reach", header="Reach", sortable=True),
                        DataTableColumn(key="follows", header="Follows", sortable=True),
                        DataTableColumn(key="saves", header="Saves", sortable=True),
                        DataTableColumn(key="shares", header="Shares", sortable=True),
                    ],
                    searchable=True,
                )

        Separator()
        with Row(gap=2):
            Badge("PoC", variant="outline")
            Text("FastMCP Apps + Meta Graph API v25.0", cssClass="text-muted-foreground text-sm")

    return PrefabApp(view=view)


async def instagram_dashboard(ig_user_id: str) -> PrefabApp:
    """Interactive Instagram analytics dashboard with charts and KPIs.

    Fetches real data from Meta Graph API and renders an interactive dashboard
    showing reach, follows per post, best posting time, and engagement metrics.

    Args:
        ig_user_id: Instagram Business/Creator account ID (e.g. "17841400438484521").
    """
    data = await _fetch_ig_data(ig_user_id)
    return _build_dashboard(data)
