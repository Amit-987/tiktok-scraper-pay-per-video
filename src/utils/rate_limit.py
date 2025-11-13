import logging
import time
from typing import Optional

logger = logging.getLogger(__name__)

def sleep_with_jitter(base_seconds: float, jitter: Optional[float] = None) -> None:
    """
    Sleep for a base amount of time, optionally adding a small jitter to avoid
    thundering-herd patterns. Kept simple for demo usage.
    """
    delay = base_seconds
    if jitter:
        delay += jitter
    logger.debug("Sleeping for %.3f seconds to respect rate limits", delay)
    time.sleep(delay)