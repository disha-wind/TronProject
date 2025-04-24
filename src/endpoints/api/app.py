from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from endpoints.api.routers import address, history
from orm import engine
from orm.core import init_db, start_mappers


@asynccontextmanager
async def lifespan(application: FastAPI):
    await init_db(engine)
    yield


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    start_mappers()

    app.include_router(address.router)
    app.include_router(history.router)

    uvicorn.run(app, host="0.0.0.0", port=8000)
