from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from document_reader import read_document
from rag_engine import local_ai

# Vi opretter selve API-serveren
app = FastAPI(
    title="Trafikstyrelsen RAG API",
    description="Lokalt, GDPR-compliant AI API til dokumentanalyse",
    version="1.0"
)

# Globale variabler til at holde AI'en i hukommelsen
llm = None
vector_db = None



# Dette kører automatisk når serveren starter
@app.on_event("startup")

def startup_event():
    global llm, vector_db
    print("Starter AI-motoren op og indlæser dokumenter...")
    data_file = "data/karakter.pdf"
    dokument = read_document(data_file)
    if dokument:
        llm, vector_db = local_ai(dokument)
        print("API Server er klar! Lytter efter spørgsmål...")
    else:
        print("Fejl: Kunne ikke indlæse dokumentet.")


# Vi fortæller  FastAPI, at dataen skal sendes indkapslet som et skjult JSON-datapakke (et Request Body), som er standarden for POST-kald
class Spørgsmål(BaseModel):
    tekst: str
    medarbejder_id: int
    haster: bool


# Vores 'Endpoint' (Den web-adresse, systemet kan spørge)
@app.post("/ask")
def ask_question(question: Spørgsmål):
    if not vector_db or not llm:
        raise HTTPException(status_code=500, detail="AI'en er ikke klar endnu.")

    # 1. Søg i databasen
    relevant_document = vector_db.similarity_search(question.tekst, k=12)

    # 2. Udtræk kilder (Guardrails)
    kilder = list(set([doc.metadata.get('source', 'Ukendt kilde') for doc in relevant_document]))

    # 3. Prompt
    prompt = f"""Spørgsmål: {question.tekst}

    Kontekst: {relevant_document}

    Instruktion:
    1. Er svaret på spørgsmålet i konteksten? Hvis JA, så svar ud fra konteksten.
    2. Hvis NEJ, så ignorér konteksten. Skriv ordet "[EGEN_VIDEN]" og giv derefter et rigtigt svar på spørgsmålet ud fra din generelle viden. Nævn ikke konteksten.

    Svar:"""

    # 4. Spørg modellen
    svar = llm.invoke(prompt)

    # Tjekker om AI 'en brugte sin egen viden (vores "guardrail")
    if "[EGEN_VIDEN]" in svar:
        kilder = []
        svar = svar.replace("[EGEN_VIDEN]", "").strip()

    # Returner struktureret JSON-svar
    return {
        "spørgsmål": question.tekst,
        "svar": svar,
        "kilder": kilder
    }