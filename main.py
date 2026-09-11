import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.ingestion.parser import parser
from src.routers.research import rag_router
load_dotenv()

chunks = parser()
app = FastAPI(debug=os.getenv("DEBUG", "False").lower() == "true")
app.include_router(rag_router)
