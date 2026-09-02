
import bm25s
from src.ingestion.parser import collection

def bm25_retrieve(query):
    all_docs = collection.get()["documents"]
    corpus_tokens = bm25s.tokenize(all_docs)
    retriever = bm25s.BM25(corpus=all_docs)
    retriever.index(corpus_tokens)
    query_tokens = bm25s.tokenize(query)
    docs, scores = retriever.retrieve(query_tokens, k=10)
    return docs[0]

