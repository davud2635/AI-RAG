from document_reader import read_document
from rag_engine import lokal_ai

data_file = "data/karakter.pdf"

dokument = read_document(data_file)

if not dokument:
    print("Kunne ikke indlæse dokumentet. Lukker programmet.")
    exit()


llm , vector_db = lokal_ai(dokument)


while True:
    user_question = input("Dit spørgsmål: ")

    if user_question.lower() == ["exit", "quit", "afslut"]:
        print("Afslutter terminalen..")
        break

    print("Tænker  ")

    relvant_document = vector_db.similarity_search(user_question, k=12)

    prompt = f"Answer only based on the context {relvant_document}. Question: {user_question}"
    answer = llm.invoke(prompt)
    print(f"\n {answer}:\n ")