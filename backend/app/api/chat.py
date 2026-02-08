from fastapi import APIRouter, HTTPException

from backend.app.api.schemas import ChatRequest, ChatResponse
from backend.app.services.ollama_client import OllamaClient

from backend.app.security.manager import SecurityManager
from backend.app.security.logger import SecurityLogger

from backend.app.dlp.manager import DLPManager
from backend.app.audit.logger import AuditLogger


router = APIRouter()

ollama = OllamaClient()
security = SecurityManager()
logger = SecurityLogger()
dlp = DLPManager()
audit = AuditLogger()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    prompt = request.prompt
    model = request.model

    if not prompt.strip():

        audit.log(
            prompt,
            model,
            "FAILED",
            "EMPTY_PROMPT"
        )

        raise HTTPException(status_code=400, detail="Prompt is empty")

    # 1. Prompt security
    try:

        security.validate_prompt(prompt)

    except ValueError as e:

        logger.log_violation("PROMPT", str(e))

        audit.log(
            prompt,
            model,
            "BLOCKED",
            "PROMPT_POLICY",
            str(e)
        )

        raise HTTPException(
            status_code=403,
            detail="Prompt blocked by security policy"
        )

    # 2. Call LLM
    try:

        result = ollama.generate(
            model=model,
            prompt=prompt
        )

    except Exception as e:

        audit.log(
            prompt,
            model,
            "FAILED",
            "LLM_ERROR",
            str(e)
        )

        raise HTTPException(status_code=500, detail=str(e))

    # 3. Output security
    try:

        security.validate_output(result)

    except ValueError as e:

        logger.log_violation("OUTPUT", str(e))

        audit.log(
            prompt,
            model,
            "BLOCKED",
            "OUTPUT_POLICY",
            str(e)
        )

        raise HTTPException(
            status_code=403,
            detail="LLM output blocked by security policy"
        )

    # 4. DLP
    dlp_result = dlp.process(result)

    if dlp_result["redacted"]:

        audit.log(
            prompt,
            model,
            "REDACTED",
            "DLP",
            str(dlp_result["violations"])
        )

    else:

        audit.log(
            prompt,
            model,
            "SUCCESS",
            "ALLOWED"
        )

    return ChatResponse(response=dlp_result["output"])
