import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.ingestion.parser import parser
load_dotenv()
app = FastAPI(debug=os.getenv("DEBUG", "False").lower() == "true")
# parser()