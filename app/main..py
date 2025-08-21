from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.fetcher import Fetcher
from app.manager import Manager


fetch = Fetcher()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await fetch.open_conn()
    yield
    await fetch.close_conn()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/data")
async def get_data():
    return await Manager.code_flow()




