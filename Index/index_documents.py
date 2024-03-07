'''
Création de l'index des documents pour le système de recherche de documents intelligents.

@Auteur: Camillia
@Temps de création: 2024-03-07 10:40:05
@Modifié par: Camillia
@Temps de modification: 2024-03-07 11:14:04
'''

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
import os
import textract


def create_index(docs_folder, index_folder):
    
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
                print(f"Erreur lors du traitement du document {file}: {e}")

    writer.commit()

docs_folder = "Document"

index_folder = "Index"

create_index(docs_folder, index_folder)
