from unittest import IsolatedAsyncioTestCase
from croydon.config import DatabaseConfig
from croydon import ctx
from croydon.cache import TraceCache


class MongoMockTest(IsolatedAsyncioTestCase):

    tc1: TraceCache
    _wrk: "Worker" = None

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        ctx.db.reconfigure(DatabaseConfig(), mock=True)

        # We don't use any database for tests, so it makes no sense
        # to use any persistent cache.
        ctx._cache_l1 = TraceCache()
        ctx._cache_l2 = TraceCache()
        cls.tc1 = ctx._cache_l1

    @property
    def wrk(self):
        from app.tasks.worker import Worker
        if self._wrk is None:
            self._wrk = Worker()
        return self._wrk

    async def run_tasks(self):
        async for task in ctx.queue.tasks(no_block=True):
            await self.wrk.run_task(task)
