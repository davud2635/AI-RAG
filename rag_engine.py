from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


def local_ai(documents):
    """
    chunk_size:  Hvor meget tekst der er i hvert stykke
    chunk_overlap: Hvor meget tekst der gentages fra tidligere stykke i den nye

    :param documents:
    :return: llm, vector_db
    """
    # Dette er en simpel split af teksten, i små bid, fra dokumentet.
    chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(documents)

    # Her bruger jeg AI-modellen (Lokalt via Ollama)
    llm = OllamaLLM(model="llama3")

    # Omdanner tekst til tal, så AI'en kan finde lignende tekst
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    # Vi har ikke brug for en stor database nu , derfor bruger jeg bare et lille lokalt vektordatabase
    vector_db = Chroma.from_documents(documents=chunks, embedding=embeddings)

    return llm, vector_db