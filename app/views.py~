from flask import render_template, request, redirect, url_for
from app import app
from elasticsearch import Elasticsearch
from .file_parse import parse_docx, parse_txt, parse_pdf, es
import os

#https://elasticsearch-py.readthedocs.io/en/master/
index_name = "search_index"

host = "http://localhost:9200"

es = Elasticsearch(host)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route("/upload",methods=["GET","POST"])
def upload():
    file_obj = request.files["file"]
    if file_obj:
        file_type = file_obj.filename.split(".")[-1]
        file_obj.save(os.path.join(app.config["UPLOAD_FOLDER"], file_obj.filename))
        if file_type == "docx":
            parse_docx(file_obj.filename)
        elif file_type == "txt":
            parse_txt(file_obj.filename)
        elif file_type == 'pdf' or file_type == 'png':
            print("got here")
            parse_pdf(file_obj.filename)        
    else:
        return redirect(url_for("index"))
    return render_template("index.html")

#how to do search courtesy of: https://marcobonzanini.com/2015/02/02/how-to-query-elasticsearch-with-python/
@app.route('/search', methods=['GET','POST'])
def search():
    query = request.form.get("query")
    results = es.search(index=index_name,body={"query":{"match": {"text":query}}})
    return render_template('results.html', results=results)

