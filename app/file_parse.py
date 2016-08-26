from docx import Document
from elasticsearch import Elasticsearch
import os

host = "http://localhost:9200"

es = Elasticsearch(host)

def parse_docx(file_name):
    os.chdir("files_to_index")
    doc = Document(file_name)
    data = {}
    data["text"] = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    es.index(index="my_index", doc_type="docx", body=data)

def parse_txt(file_name):
    os.chdir("files_to_index")
    with open(file_name,"r") as f:
        data = {}
        data["text"] = f.read()
        es.index(index="my_index", doc_type="txt", body=data)
