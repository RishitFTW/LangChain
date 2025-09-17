from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('ML-book.pdf')
docs= loader.load()

print(docs[1].page_content)