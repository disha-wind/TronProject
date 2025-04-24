from fastapi import FastAPI
from endpoints.api.routers import address, history

app = FastAPI()

app.include_router(address.router)
app.include_router(history.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
