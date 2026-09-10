import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.ingestion.parser import parser
from src.services.rag import rag
load_dotenv()

chunks = parser()
app = FastAPI(debug=os.getenv("DEBUG", "False").lower() == "true")
rag("what is attention ?")  