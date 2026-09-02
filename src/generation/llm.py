from langchain_ollama import ChatOllama

def search(reranked , query):

    prompt = f"""
        You are a helpful AI assistant answering questions using retrieved documents.

        Use the provided context to answer the user's question.

        Rules:
        - Answer based only on the information contained in the context.
        - Do not use your own knowledge to fill in missing information.
        - If the context does not contain enough information to answer the question, say:
        "I don't have enough information in the provided context to answer that."
        - Do not invent or hallucinate facts.
        - Give a clear and concise answer.
        - When useful, explain the answer using relevant details from the context.

        Context:
        {reranked}

        Question:
        {query}

        Answer:
    """

    llm = ChatOllama(
            model="qwen",
            temperature=0,
        )

    ai_msg = llm.invoke(prompt)

    return ai_msg.content