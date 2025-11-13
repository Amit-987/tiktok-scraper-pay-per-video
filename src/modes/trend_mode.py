from __future__ import annotations

import logging
from typing import Any, Dict, List

from config import Config
from client.tiktok_api_client import TikTokApiClient

logger = logging.getLogger(__name__)

def run(config: Config, client: TikTokApiClient) -> List[Dict[str, Any]]:
    logger.info("Executing TREND mode for region=%s", config.region or "ALL")
    items = client.fetch_trend(
        region=config.region,
        max_items=config.max_items,
        is_unlimited=config.is_unlimited,
    )
    return items