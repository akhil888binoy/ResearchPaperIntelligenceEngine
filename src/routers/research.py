from fastapi import APIRouter, Depends, HTTPException
from src.services.rag import rag

rag_router = APIRouter(
    prefix="/api/rag",
    tags=["rag"]
)


@rag_router.post("/query" , status_code=201)
def query(query : str):
    return rag(query)
