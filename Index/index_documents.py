'''
Creation of the document index for the smart document retrieval system.

@author: Camillia
@create_time: 2024-03-07 10:40:05
@modified_by: Camillia
@modified_time: 2024-03-07 11:20:04
'''

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
import os
import textract

def create_index(docs_folder, index_folder):
    """
    Function to create the document index.

    :param docs_folder: The path of the folder containing the documents.
    :param index_folder: The path of the folder where the index will be stored.
    """
    schema = Schema(title=TEXT(stored=True), content=TEXT())

    if not os.path.exists(index_folder):
        os.mkdir(index_folder)

    ix = create_in(index_folder, schema)
    writer = ix.writer()

    for root, dirs, files in os.walk(docs_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                text = textract.process(file_path).decode('utf-8')
                writer.add_document(title=file, content=text)
            except Exception as e:
                print(f"Error processing document {file}: {e}")

    writer.commit()

docs_folder = "../Document"
index_folder = "Index"

create_index(docs_folder, index_folder)
