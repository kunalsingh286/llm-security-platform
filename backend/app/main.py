from fastapi import FastAPI
from backend.app.api.chat import router as chat_router


app = FastAPI(
    title="LLM Security Platform",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(chat_router)
