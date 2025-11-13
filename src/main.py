import argparse
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

from config import Config, load_config_from_args
from client.tiktok_api_client import TikTokApiClient
from outputs.dataset_writer import DatasetWriter
from utils.logging_utils import configure_logging
from modes import (
    search_mode,
    trend_mode,
    hashtag_mode,
    user_mode,
    music_mode,
)

MODES = {
    "SEARCH": search_mode.run,
    "TREND": trend_mode.run,
    "HASHTAG": hashtag_mode.run,
    "USER": user_mode.run,
    "MUSIC": music_mode.run,
}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fast TikTok Scraper (Pay per Result) – local integration runner"
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=list(MODES.keys()),
        help="Scraping mode: SEARCH, TREND, HASHTAG, USER, or MUSIC",
    )
    parser.add_argument(
        "--keyword",
        help="Keyword for SEARCH mode",
    )
    parser.add_argument(
        "--region",
        help="2-letter region code (e.g. US, GB, VN) used by TREND and SEARCH",
    )
    parser.add_argument(
        "--hashtag-url",
        dest="hashtag_url",
        help="Hashtag URL for HASHTAG mode",
    )
    parser.add_argument(
        "--user-url",
        dest="user_url",
        help="User profile URL for USER mode",
    )
    parser.add_argument(
        "--music-url",
        dest="music_url",
        help="Music track URL for MUSIC mode",
    )
    parser.add_argument(
        "--max-items",
        dest="max_items",
        type=int,
        default=100,
        help="Soft limit of videos to collect",
    )
    parser.add_argument(
        "--unlimited",
        dest="is_unlimited",
        action="store_true",
        help="Attempt to collect all available items (ignores max-items soft cap)",
    )
    parser.add_argument(
        "--input",
        dest="input_path",
        default="data/sample_output.json",
        help="Path to input JSON used by the local demo client",
    )
    parser.add_argument(
        "--output",
        dest="output_path",
        default="data/output.json",
        help="Path where normalized output JSON will be stored",
    )
    parser.add_argument(
        "--log-level",
        dest="log_level",
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR)",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = load_config_from_args(args)
    configure_logging(config.log_level)
    logger = logging.getLogger(__name__)

    logger.info("Starting Fast TikTok Scraper local runner")
    logger.debug("Resolved config: %s", config)

    project_root = Path(__file__).resolve().parents[1]
    client = TikTokApiClient(project_root=project_root)
    writer = DatasetWriter(output_path=project_root / config.output_path)

    mode_fn = MODES.get(config.type)
    if not mode_fn:
        raise ValueError(f"Unsupported scraping type: {config.type}")

    logger.info("Running mode=%s", config.type)
    items: List[Dict[str, Any]] = mode_fn(config=config, client=client)
    logger.info("Collected %d raw items", len(items))

    writer.write(items)
    logger.info("Dataset written to %s", writer.output_path)

if __name__ == "__main__":
    main()