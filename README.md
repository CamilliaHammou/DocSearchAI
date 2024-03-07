# DocSearchAI

DocSearchAI is an intelligent document search system that allows you to quickly find documents based on keywords from a set of documents. This project utilizes indexing and search techniques to provide relevant and fast results.

## Features

- Document indexing for quick search
- Keyword-based document search
- Support for various file formats including PDF, DOCX, etc.
- User-friendly interface

## Installation

1. Ensure you have Python 3.6 or later installed on your system.
2. Clone this GitHub repository to your local machine.

## Usage

Add your documents to the Document folder.
Create the index by running the index_documents.py script.
```bash
python3 index_documents.py
```
To search for documents, run the search_documents.py script and enter your search query.
```bash
python3 search_documents.py
```
## Examples

Here are some examples of search queries you can try:

```bash
(myenv) ➜  Index git:(main) ✗ python3 search_documents.py                                         

Enter your search query : esgi

Title: CV_CamilliaHAMMOU_altrn.pdf
Relevance: 1.5076174477205586

Title: SynthèseOpen_HAMMOU.pdf
Relevance: 0.7509594021409817
```
Title: This represents the title of the document that matches the search query. In the example provided, "CV_CamilliaHAMMOU_altrn.pdf" and "SynthèseOpen_HAMMOU.pdf" are the titles of the documents retrieved from the search.

Relevance: This indicates the relevance score of each document to the search query.The higher the relevance score, the more closely the document matches the search query.

Happy document searching!





Camillia HAMMOU




