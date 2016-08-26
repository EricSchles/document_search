from docx import Document
from elasticsearch import Elasticsearch
import os

host = "http://localhost:9200"

es = Elasticsearch(host)
index_name = "search_index"

def parse_docx(file_name):
    os.chdir("app/files_to_index")
    doc = Document(file_name)
    data = {}
    data["text"] = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    data["title"] = file_name
    es.index(index=index_name, doc_type="docx", body=data)

def parse_txt(file_name):
    os.chdir("app/files_to_index")
    with open(file_name,"r") as f:
        data = {}
        data["text"] = f.read()
        data["title"] = file_name
        es.index(index=index_name, doc_type="txt", body=data)
