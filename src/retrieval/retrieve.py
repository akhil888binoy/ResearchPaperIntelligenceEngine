from src.ingestion.parser import collection , convert_to_vector



def retrieval(query):

    embed_query = convert_to_vector(query)

    results = collection.query(
        query_embeddings=[embed_query], # Chroma will embed this for you
        n_results=10 # how many results to return
    )
    
        
    return  results['documents'][0] 