from src.ingestion.parser import collection , convert_to_vector
from src.generation.llm import client

async def rewrite_query(query):
    prompt = f"""
    Rewrite the following user question into a clear,
    specific search query for retrieving relevant documents.

    Keep the original meaning.
    Do not answer the question.

    Question:
    {query}

    Rewritten query:
    """

    response = await client.chat(
        model="qwen",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]


async def retrieval(query):

    embed_query = await convert_to_vector(query)

    results = await collection.query(
        query_embeddings=[embed_query], # Chroma will embed this for you
        n_results=10 # how many results to return
    )

    #Relevancy Gate
    relevant = False
    for d in results['distances']:
        if d < 0.8:
            relevant = True
            break    
    if not relevant:
        return "No relevant context"
        
    return  results['documents'][0] 