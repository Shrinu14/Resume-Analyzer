# app/db.py

from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
db = client["resume_analyzer"]
collection = db["resumes"]

def save_resume(resume_data: dict):
    collection.insert_one(resume_data)

def get_all_resumes():
    return list(collection.find({}))
