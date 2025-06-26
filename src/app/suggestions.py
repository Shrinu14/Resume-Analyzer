# app/suggestions.py

from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.1", base_url="http://host.docker.internal:11434")


def get_resume_improvement_tips(resume_text: str) -> str:
    prompt = f"""
You are an expert resume reviewer.

Analyze the following resume and give exactly 3 specific suggestions to improve it. Focus on tone, formatting, and content.

Resume:
{resume_text}
"""
    return llm.invoke(prompt)
