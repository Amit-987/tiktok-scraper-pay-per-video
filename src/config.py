from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    type: str
    region: Optional[str] = None
    keyword: Optional[str] = None
    hashtag_url: Optional[str] = None
    user_url: Optional[str] = None
    music_url: Optional[str] = None
    max_items: int = 100
    is_unlimited: bool = False
    input_path: str = "data/sample_output.json"
    output_path: str = "data/output.json"
    log_level: str = "INFO"

def load_config_from_args(args: argparse.Namespace) -> Config:
    """Create Config from parsed CLI args, falling back to environment variables where useful."""
    return Config(
        type=args.type.upper(),
        region=args.region or os.getenv("TTS_REGION"),
        keyword=args.keyword or os.getenv("TTS_KEYWORD"),
        hashtag_url=args.hashtag_url or os.getenv("TTS_HASHTAG_URL"),
        user_url=args.user_url or os.getenv("TTS_USER_URL"),
        music_url=args.music_url or os.getenv("TTS_MUSIC_URL"),
        max_items=args.max_items or int(os.getenv("TTS_MAX_ITEMS", "100")),
        is_unlimited=bool(args.is_unlimited or os.getenv("TTS_UNLIMITED", "false").lower() == "true"),
        input_path=args.input_path or os.getenv("TTS_INPUT_PATH", "data/sample_output.json"),
        output_path=args.output_path or os.getenv("TTS_OUTPUT_PATH", "data/output.json"),
        log_level=args.log_level or os.getenv("TTS_LOG_LEVEL", "INFO"),
    )