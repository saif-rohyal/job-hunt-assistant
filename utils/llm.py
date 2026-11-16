
from crewai import LLM
from utils.config import GEMINI_API_KEY

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=GEMINI_API_KEY,
    temperature=0.3,
)
