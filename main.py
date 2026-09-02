import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.ingestion.parser import parser
from src.retrieval.retrieve import retrieval
from src.generation.llm import search
from src.reranking.reranker import rerank
from src.retrieval.bm25_retrieve import bm25_retrieve
from src.reranking.reranker import rrf
load_dotenv()


app = FastAPI(debug=os.getenv("DEBUG", "False").lower() == "true")

chunks = parser()
query = "What is capital of india?"
vector_docs  = retrieval(query)

# ADD RELEVANCE GATE
# relevant = False

    # for r in reranked:
    #     if r.relevance_score >= 0.5:
    #         relevant = True
    #         break

    # if not relevant:
    #     return "No relevant context"


bm25_docs  = bm25_retrieve(query)
ranked_docs = rrf(vector_docs=vector_docs , bm25_docs=bm25_docs)


reranked = rerank( ranked_docs , query)


# print(context)
# print(query)

msg = search( ranked_docs, query )
print(msg)      