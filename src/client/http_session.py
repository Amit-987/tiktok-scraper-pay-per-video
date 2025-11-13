import logging
from typing import Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

def create_retrying_session(
    total: int = 3,
    backoff_factor: float = 0.3,
    status_forcelist: Optional[list[int]] = None,
    timeout: int = 10,
) -> requests.Session:
    """
    Create a requests.Session with basic retry logic.
    This module is included for future real HTTP integration; it is not used by the
    local demo client but remains ready for production usage.
    """
    if status_forcelist is None:
        status_forcelist = [500, 502, 503, 504]

    session = requests.Session()
    retry = Retry(
        total=total,
        read=total,
        connect=total,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
        allowed_methods=frozenset(["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Attach a default timeout to all requests by wrapping session.request
    original_request = session.request

    def request_with_timeout(method, url, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = timeout
        logger.debug("HTTP %s %s", method, url)
        return original_request(method, url, **kwargs)

    session.request = request_with_timeout  # type hint: ignore[attr-defined]
    return session