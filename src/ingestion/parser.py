from pypdf import PdfReader
import re
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
import ollama
from langchain_community import document_loaders
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
import uuid
import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="research_papers")

def convert_to_vector(texts):
    
    try:

        response = ollama.embed(
                model  =  'qwen',
                input =  texts,
        )

        return np.array(response["embeddings"][0])

    except Exception as e:

        print("An error occurred:", e)

    return np.array([]) 


text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100,
    chunk_overlap=50,
)




def parser():

    documents = document_loaders.PyPDFLoader('docs/attentionallyouneed.pdf').load()

    doc_splits = text_splitter.split_documents(documents)

    collections= {
        "ids":[],
        "documents": [],
        "embeddings":[],
        "metadatas":[]
    }

    for doc  in doc_splits:
        text= doc.page_content
        metadata = doc.metadata

        embeddings = convert_to_vector(doc.page_content)
        collections['ids'].append(str(uuid.uuid1()))
        collections['documents'].append(text)
        collections['embeddings'].append(embeddings)
        collections['metadatas'].append(metadata)

    collection.add(**collections)


    




