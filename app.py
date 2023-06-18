from flask import Flask, render_template, request, json

from elasticsearch import Elasticsearch
import json

es = Elasticsearch("http://localhost:9200",http_auth= ('elastic', 'password'))


# user defined function
def search_index(search_string):
    result = es.search(index='catalog_index', size=1000, query= {"multi_match": {"query": search_string, "fields": ["title", "description", 'contactName']}})
    result = result.body
    result['search_string']= search_string
    return result


def search_all():
    result = es.search(index="catalog_index", size=1000, body={"query": {"match_all": {}}})
    return result


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.to_dict()['search_box']
        results = search_index(search_term)
        return render_template('search.html', results=results)
    return render_template('welcome.html')


@app.route('/search_all', methods=['GET', 'POST'])
def search_complete():
    results = search_all()
    return render_template('search_all.html', results=results)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
