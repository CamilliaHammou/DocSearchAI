'''
 # @ Author: Camillia
 # @ Create Time: 2024-03-07 11:50:16
 # @ Modified by: Camillia
 # @ Modified time: 2024-03-07 11:17:39
 '''

from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def search_documents(query_string, index_folder):
    ix = open_dir(index_folder)
    searcher = ix.searcher()
    parser = QueryParser("content", ix.schema)
    query = parser.parse(query_string)
    results = searcher.search(query)
    return results

query_string = input("Entrez votre requête de recherche : ")
results = search_documents(query_string, "Index")

for result in results:
    print("Titre:", result["title"])
    print("Pertinance:", result.score)
    print()
