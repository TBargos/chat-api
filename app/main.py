from fastapi import FastAPI
from app.routers import chats, messages


app = FastAPI(
    title="Chat API",
    version="0.1.0",
)

app.include_router(chats.router)
app.include_router(messages.router)


@app.get("/health")
def healthcheck():
    return {"status": "ok"}