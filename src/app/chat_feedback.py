from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.1", base_url="http://host.docker.internal:11434")

def get_resume_feedback(text: str) -> str:
    prompt = f"""
You are a resume expert. Analyze this resume and give 3 suggestions for improvement in tone, structure, or content.

Resume:
{text}
"""
    return llm.invoke(prompt)
