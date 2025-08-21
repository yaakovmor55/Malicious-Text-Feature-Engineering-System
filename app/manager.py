from app.fetcher import Fetcher
from app.processor import Processor
import asyncio


class Manager:

    @staticmethod
    async def code_flow():
        fetcher = Fetcher()
        col = await fetcher.read_collection()
        processor = Processor(col)
        processor.rare_word_in_text()
        processor.find_text_emotion()
        processor.find_weapons()
        return processor.df.to_dict(orient="records")
