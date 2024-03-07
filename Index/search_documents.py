'''
Script to search documents in the indexed repository.

@author: Camillia
@create_time: 2024-03-07 10:50:51
@modified_by: Camillia
@modified_time: 2024-03-07 11:38:39
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

query_string = input("Enter your search query : ")
results = search_documents(query_string, "Index")

for result in results:
    print("Title:", result["title"])
    print("Relevance:", result.score)
    print()
