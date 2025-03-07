from fastapi import APIRouter
from llm import Llm

router = APIRouter()

@router.get("/get-llms", response_model=list[str])
async def get_llm():
    return [m.value for m in Llm]