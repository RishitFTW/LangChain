from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader= DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs=loader.lazy_load()
print(docs[1].page_content)
