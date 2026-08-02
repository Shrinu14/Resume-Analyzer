import os
import logging

logger = logging.getLogger(__name__)

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://host.docker.internal:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

FALLBACK_MESSAGE = (
    "AI-generated suggestions are unavailable right now (no LLM backend is "
    "configured or reachable). Set OPENAI_API_KEY, or run Ollama and set "
    "OLLAMA_BASE_URL, to enable this feature."
)


def _prompt(text: str) -> str:
    return f"""
You are a resume expert. Analyze this resume and give 3 suggestions for improvement in tone, structure, or content.

Resume:
{text}
"""


def get_resume_feedback(text: str) -> str:
    """
    Returns LLM-based resume feedback. Prefers OpenAI (if OPENAI_API_KEY is
    set) and falls back to a local Ollama server. Never raises: if no
    backend is configured or reachable, returns a friendly fallback message
    instead of crashing the whole /analyze/ request (previously this had no
    error handling at all, so an unreachable Ollama server took down every
    analysis request).
    """
    prompt = _prompt(text)

    if OPENAI_API_KEY:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.warning(f"OpenAI feedback generation failed: {e}")

    try:
        from langchain_ollama import OllamaLLM

        llm = OllamaLLM(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL)
        return llm.invoke(prompt)
    except Exception as e:
        logger.warning(f"Ollama feedback generation failed: {e}")
        return FALLBACK_MESSAGE
