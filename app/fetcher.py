from typing import List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

class Fetcher:
    def __init__(self):
        self.conn: AsyncIOMotorClient | None = None
        self.soldier = None
        self.conf = Config()

    # Open connection
    def open_conn(self) -> AsyncIOMotorClient:
        if self.conn is None:
            self.conn = AsyncIOMotorClient(self.conf.MONGO_URI)
        return self.conn

    def get_collection(self):
        cli = self.open_conn()
        return cli[self.conf.MONGO_DB][self.conf.COLLECTION]

    async def read_collection(self) -> List[Dict[str, Any]]:
        col = self.get_collection()
        docs = []
        async for d in col.find({}, {"_id": 0}):
            docs.append(d)
        return docs

    async def close_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None

