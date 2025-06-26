# 🧠 AI Resume Analyzer with FastAPI + Ollama + LangChain

A production-ready, containerized application that analyzes resumes and provides intelligent suggestions using LLMs via Ollama and LangChain. It supports resume parsing, improvement tips, and language feedback using `language_tool_python`.

---

## 🚀 Features

- Upload and analyze resumes (PDF/DOCX/TXT)
- Get AI-generated suggestions for improvement (tone, structure, content)
- Grammar feedback using LanguageTool
- Powered by `llama3.1` LLM (via [Ollama](https://ollama.com))
- Built with FastAPI + Docker + LangChain
- REST API with Swagger docs
- LanguageTool + spaCy for NLP
- Ready for CI/CD pipelines

---

## 🛠 Tech Stack

| Layer        | Tools Used                             |
|--------------|----------------------------------------|
| Backend      | FastAPI, LangChain, Uvicorn            |
| LLM Inference| Ollama (LLaMA 3.1)                     |
| NLP Tools    | spaCy, LanguageTool                    |
| Parsing      | `pdfminer`, `docx`, `tesseract-ocr`    |
| Packaging    | Docker, Python 3.11                    |
| CI/CD        | GitHub Actions                         |

---

## 📦 Setup

### 1. Prerequisites

- Python 3.11+
- Docker
- [Ollama installed and running](https://ollama.com)
- (Optional) `uv` for dependency management:  
  `curl -LsSf https://astral.sh/uv/install.sh | sh`

---

### 2. Clone the repo

```bash
git clone https://github.com/Shrinu14/Resume-Analyzer.git
cd Resume-Analyzer

### 3. Run with Docker
Make sure Ollama is running at http://localhost:11434
docker build -t resume-analyzer .
docker run -p 8080:8080 resume-analyzer


### 4. Access the API
Swagger UI: http://localhost:8080/docs

Health check: GET /ping

Analyze Resume: POST /analyze/ (upload file + JD)