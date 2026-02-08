from fastapi import APIRouter, HTTPException

from backend.app.api.schemas import ChatRequest, ChatResponse
from backend.app.services.ollama_client import OllamaClient

from backend.app.security.manager import SecurityManager
from backend.app.security.logger import SecurityLogger


router = APIRouter()

ollama = OllamaClient()
security = SecurityManager()
logger = SecurityLogger()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is empty")

    # 1. Check prompt
    try:
        security.validate_prompt(request.prompt)

    except ValueError as e:

        logger.log_violation("PROMPT", str(e))

        raise HTTPException(
            status_code=403,
            detail="Prompt blocked by security policy"
        )

    # 2. Call LLM
    try:

        result = ollama.generate(
            model=request.model,
            prompt=request.prompt
        )

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))

    # 3. Check output
    try:

        security.validate_output(result)

    except ValueError as e:

        logger.log_violation("OUTPUT", str(e))

        raise HTTPException(
            status_code=403,
            detail="LLM output blocked by security policy"
        )

    return ChatResponse(response=result)
