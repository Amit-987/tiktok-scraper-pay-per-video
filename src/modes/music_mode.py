from __future__ import annotations

import logging
from typing import Any, Dict, List

from config import Config
from client.tiktok_api_client import TikTokApiClient

logger = logging.getLogger(__name__)

def run(config: Config, client: TikTokApiClient) -> List[Dict[str, Any]]:
    if not config.music_url:
        raise ValueError("MUSIC mode requires `music_url` to be set")

    logger.info("Executing MUSIC mode with url='%s'", config.music_url)
    items = client.fetch_music(
        music_url=config.music_url,
        max_items=config.max_items,
        is_unlimited=config.is_unlimited,
    )
    return items