import json
import logging
from typing import Any, Optional
import redis.asyncio as aioredis
from app.core.config import settings

logger = logging.getLogger(__name__)


class RedisManager:
    def __init__(self):
        self._client: Optional[aioredis.Redis] = None
        self._memory_cache: dict[str, Any] = {}
        self._is_connected: bool = False

    async def connect(self) -> None:
        try:
            self._client = aioredis.from_url(
                settings.REDIS_URL,
                encoding="utf-8",
                decode_responses=True,
                socket_connect_timeout=2.0
            )
            await self._client.ping()
            self._is_connected = True
            logger.info("Connected to Redis at %s", settings.REDIS_URL)
        except Exception as e:
            self._is_connected = False
            logger.warning("Could not connect to Redis (%s). Using in-memory fallback.", str(e))

    async def disconnect(self) -> None:
        if self._client and self._is_connected:
            await self._client.close()
            self._is_connected = False

    async def get(self, key: str) -> Optional[str]:
        if self._is_connected and self._client:
            try:
                return await self._client.get(key)
            except Exception:
                pass
        return self._memory_cache.get(key)

    async def set(self, key: str, value: Any, expire_seconds: Optional[int] = None) -> bool:
        str_val = value if isinstance(value, str) else json.dumps(value)
        if self._is_connected and self._client:
            try:
                if expire_seconds:
                    await self._client.setex(key, expire_seconds, str_val)
                else:
                    await self._client.set(key, str_val)
                return True
            except Exception:
                pass
        self._memory_cache[key] = str_val
        return True

    async def delete(self, key: str) -> bool:
        if self._is_connected and self._client:
            try:
                await self._client.delete(key)
            except Exception:
                pass
        self._memory_cache.pop(key, None)
        return True

    async def exists(self, key: str) -> bool:
        if self._is_connected and self._client:
            try:
                return bool(await self._client.exists(key))
            except Exception:
                pass
        return key in self._memory_cache


redis_client = RedisManager()
