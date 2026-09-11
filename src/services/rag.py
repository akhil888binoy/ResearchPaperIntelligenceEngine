from typing import List , Optional
from sqlalchemy.orm import Session
from src.retrieval.retrieve import retrieval
from src.generation.llm import search
from src.reranking.reranker import rerank
from src.retrieval.bm25_retrieve import bm25_retrieve
from src.reranking.reranker import rrf
from src.retrieval.retrieve import rewrite_query

async def rag(query: str):
    rewritten_query = await rewrite_query(query)

    vector_docs = await retrieval(rewritten_query)

    bm25_docs = bm25_retrieve(rewritten_query)

    ranked_docs = rrf(
        vector_docs=vector_docs,
        bm25_docs=bm25_docs
    )

    reranked = rerank(ranked_docs, rewritten_query)

    msg = await search(reranked, rewritten_query)

    return msg