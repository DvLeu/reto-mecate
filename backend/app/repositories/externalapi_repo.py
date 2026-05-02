import httpx 
from app.core.config import config

class StackOverflowRepo:
    async def fetch_questions(self) -> list[dict]:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(config.STACK_API_URL)
            response.raise_for_status()
            return response.json().get("items", [])