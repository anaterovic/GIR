import json
from argparse import ArgumentParser

from elasticsearch import Elasticsearch
from flask import Flask, request

from ir_exercise import logger
from ir_exercise.constants import INDEX_NAME

HOST = "0.0.0.0"
PORT = 6000
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

TEXT = "text"
SIZE = "size"
DOCS = "documents"
SEARCH_INDEX = INDEX_NAME


def create_query(query_str: str):
    # Todo:
    #  Make your query better by discovering search features, e.g.:
    #  - differences between 'should' and 'must'
    #  - boosting fields
    #  - ...
    #  More details
    #  - https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html
    #  - https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-boosting-query.html
    query = {
        "bool": {
            "should": [
                {"match": {"cast": {"query":query_str, "boost":2}}},
                {"match": {"summary": {"query":query_str, "boost":2}}},
                {"match": {"plot": query_str}},
                {"match": {"filming": query_str}},
                {"match": {"awards": query_str}},  
                {"match": {"production": query_str}},
                {"match": {"title": {"query":query_str, "boost":100}}},
                {"regexp":{"title":{
                    "value":".*"+query_str+".*",
                    "case_insensitive": True,
                    "boost":50}}    
                }
            ],
        }
    }
    return query


class Searcher:
    def __init__(self):
        self.es_client = Elasticsearch(
            ["http://localhost:9200"],
        )
        self.default_size = 10

    def search(self, query_str: str, size: int = None):
        response = {DOCS: []}
        query = create_query(query_str)
        logger.info(f"Executing query:\n{json.dumps(query, indent=2)}\non index {SEARCH_INDEX}")
        result = self.es_client.search(index=SEARCH_INDEX, query=query)
        if size is None:
            size = self.default_size
        response[DOCS] = result["hits"]["hits"][:size]
        logger.info(
            f"Retrieving first {size} hits:\n{json.dumps([doc['_id'] for doc in response[DOCS]], indent=2)}"
        )
        return response


@app.route("/ir-search-service", methods=["GET"])
def search():
    data = request.json
    searcher = Searcher()
    size = data[SIZE] if SIZE in data else None
    return searcher.search(query_str=data[TEXT], size=size)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--index",
        default=INDEX_NAME,
        help=f"Name of the index. If left empty it defaults to '{INDEX_NAME}'.",
    )
    args = parser.parse_args()
    SEARCH_INDEX = args.index
    logger.info(f"Index is set to {SEARCH_INDEX}")
    app.run(debug=True, host=HOST, port=PORT)
