from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from tempfile import NamedTemporaryFile
from main import analyze_resume_pipeline
from src.app.utils import infer_file_type

app = FastAPI(
    title="Resume Analyzer API",
    version="1.0.0",
    description="Analyze resumes and match them to job descriptions"
)

# Allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...), jd_text: str = Form(...)):
    """
    Accepts a resume file and a job description (text), returns analysis result.
    """
    file_type = infer_file_type(file.filename)

    with NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    result = analyze_resume_pipeline(tmp_path, file_type, jd_text)
    return result
