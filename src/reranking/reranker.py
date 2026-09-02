import voyageai
import os
from dotenv import load_dotenv

load_dotenv()
VOYAGE_API_KEY = os.getenv('VOYAGE_API_KEY')

vo = voyageai.Client(api_key=VOYAGE_API_KEY)


def rrf(vector_docs, bm25_docs, k=60):
    scores = {}

    for rank, doc in enumerate(vector_docs, start=1):
        scores[doc] = scores.get(doc, 0) + 1 / (k + rank)

    for rank, doc in enumerate(bm25_docs, start=1):
        scores[doc] = scores.get(doc, 0) + 1 / (k + rank)

    ranked_docs = sorted(
        scores,
        key=scores.get,
        reverse=True
    )

    return ranked_docs


def rerank(ranked_docs ,query):


    reranking = vo.rerank(query, ranked_docs, model="rerank-2.5", top_k=3)

    return reranking
    


