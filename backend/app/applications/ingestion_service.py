"""
Job Ingestion Service with Bounded Pagination & Anti-Infinite Loop Guards.
"""

from typing import List, Dict, Any, Optional, Set, Callable
import logging

logger = logging.getLogger(__name__)


class BoundedPaginationError(Exception):
    pass


class JobIngestionService:
    """
    Safely ingests external job requisitions or applicant queues with strict bounds,
    cycle detection, and empty-page early termination to prevent runaway 50K+ loops.
    """

    MAX_PAGES_DEFAULT: int = 100
    MAX_ITEMS_PER_BATCH: int = 5000

    @classmethod
    def sync_feed(
        cls,
        fetch_page_fn: Callable[[int, Optional[str]], Dict[str, Any]],
        max_pages: int = MAX_PAGES_DEFAULT,
        max_items: int = MAX_ITEMS_PER_BATCH
    ) -> List[Dict[str, Any]]:
        """
        Paginates through upstream feeds with 4 safety circuit-breakers:
        1. Hard ceiling on max_pages (default 100).
        2. Immediate break on empty page payload (`items == []`).
        3. Cursor cycle / duplicate page token detection.
        4. Hard cap on max total items.
        """
        all_items: List[Dict[str, Any]] = []
        visited_tokens: Set[str] = set()
        page_num = 1
        next_token: Optional[str] = None

        while page_num <= max_pages:
            response = fetch_page_fn(page_num, next_token)
            items = response.get("items", [])

            # Circuit breaker 1: Empty page terminates immediately
            if not items:
                logger.info(f"Ingestion terminated cleanly at page {page_num}: empty page encountered.")
                break

            all_items.extend(items)

            # Circuit breaker 2: Max item ceiling
            if len(all_items) >= max_items:
                all_items = all_items[:max_items]
                logger.warning(f"Ingestion reached max items cap ({max_items}). Halting pagination.")
                break

            # Circuit breaker 3: Check next page token / cursor
            next_token = response.get("next_token")
            has_more = response.get("has_more", False)

            if not has_more or not next_token:
                break

            if next_token in visited_tokens:
                logger.error(f"Circular page token detected ('{next_token}'). Breaking infinite loop.")
                break

            visited_tokens.add(next_token)
            page_num += 1

        return all_items
