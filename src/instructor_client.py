import os

import instructor
from openai import AsyncOpenAI


def get_model_name() -> str:
    return (os.getenv("GBIF_MODEL") or "gpt-4o-mini").strip()


async def get_client():
    return instructor.from_openai(AsyncOpenAI(), model=get_model_name())
