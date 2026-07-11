
from langchain_community.document_loaders import TextLoader, CSVLoader, PDFPlumberLoader
import os

def read_document(file_path):
    filnavn, filtype = os.path.splitext(file_path)
    if filtype == ".pdf":
        return PDFPlumberLoader(file_path).load()
    elif filtype == ".csv":
        return CSVLoader(file_path).load()
    elif filtype == ".txt":
        return TextLoader(file_path).load()
    else:
        print("File type not supported")
        return []