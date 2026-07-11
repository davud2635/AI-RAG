from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


def lokal_ai(dokumenter):
    # Dette er en simpel split af teksten, i små bid, fra dokumentet.
    chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(dokumenter)

    # Her opretter jeg AI-modellerne (Lokalt via Ollama)
    llm = OllamaLLM(model="llama3")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Vi har ikke brug for en stor database nu , derfor bruger jeg bare et lille lokalt vektordatabase
    vector_db = Chroma.from_documents(documents=chunks, embedding=embeddings)

    return llm, vector_db