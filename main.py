from document_reader import read_document
from rag_engine import local_ai

data_file = "data/karakter.pdf"

dokument = read_document(data_file)

if not dokument:
    print("Kunne ikke indlæse dokumentet. Lukker programmet.")
    exit()


llm , vector_db = local_ai(dokument)


while True:
    user_question = input("Dit spørgsmål: ")

    if user_question.lower().strip() in ["exit", "quit", "afslut"]:
        print("Afslutter terminalen..")
        break

    print("Tænker...")

    relevant_documents = vector_db.similarity_search(user_question, k=12)

    # Udtrækker filnavnene på de dokumenter, AI'en har brugt til sit svar
    kilder = set([doc.metadata.get('source', 'Ukendt kilde') for doc in relevant_documents])
    print(f"AI'en baserer sit svar på følgende dokumenter: {kilder}")

    prompt = f"Answer only based on the context {relevant_documents}. Question: {user_question}"
    answer = llm.invoke(prompt)
    print(f"\n {answer}:\n ")