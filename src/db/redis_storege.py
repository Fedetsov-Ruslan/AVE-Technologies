from redis.asyncio import ConnectionPool, Redis

from config import redis_settings


class RedisClient(Redis):
    def __init__(self):
        self._pool = ConnectionPool(
            host=redis_settings.REDIS_HOST,
            port=redis_settings.REDIS_PORT,
            password=redis_settings.REDIS_PASSWORD,
            decode_responses=True
        )
        super().__init__(connection_pool=self._pool)

    async def close(self):
        await super().close()
        if self._pool:
            await self._pool.disconnect()

redis_client = RedisClient()
