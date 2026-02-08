from fastapi import APIRouter, HTTPException
from backend.app.api.schemas import ChatRequest, ChatResponse
from backend.app.services.ollama_client import OllamaClient


router = APIRouter()
ollama = OllamaClient()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is empty")

    try:
        result = ollama.generate(
            model=request.model,
            prompt=request.prompt
        )

        return ChatResponse(response=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
