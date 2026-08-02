###############################
#   Resume-Analyzer Backend   #
#   Dockerfile (configurable) #
###############################

# ---- Base image ----
FROM python:3.11-slim

# ---- Environment ----
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/root/.local/bin:$PATH" \
    PYTHONPATH=/app \
    PORT=8001                
WORKDIR /app

# ---- OS packages (Java + OCR deps) ----
RUN apt-get update && apt-get install -y \
    default-jre-headless \
    tesseract-ocr \
    poppler-utils \
    libgl1 \
    build-essential \
    curl \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# ---- Install uv (faster pip) ----
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# ---- Copy project ----
COPY . .

# ---- Python dependencies ----
RUN uv pip install --system --no-cache-dir -r requirements.txt

# ---- spaCy model ----
RUN python -m spacy download en_core_web_sm

# ---- Expose configurable port ----
EXPOSE ${PORT}

# ---- Start FastAPI ----
CMD ["sh", "-c", "uvicorn src.app.api:app --host 0.0.0.0 --port $PORT"]
