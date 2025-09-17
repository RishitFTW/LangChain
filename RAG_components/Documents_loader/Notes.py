# Document loaders are components in LangChain used to load data from various sources into a
# standardized format (usually as Document objects), which can then be used for chunking,
# embedding, retrieval, and generation              
# Document(
#     page_content="The actual text content",
#     metadata={"source": "filename.pdf", ...}
# )
# Link to Docs => https://python.langchain.com/docs/concepts/document_loaders/


#                         ------------------
#                         | DocumentLoaders |
#                         ------------------
#                           /    |     |     \
#                          /     |     |      \
#                         v      v     v       v
#    -------------   -------------   -------------   -------------
#    | TextLoader |   | PyPDFLoader |   | WebBaseLoader |   | CSVLoader |
#    -------------   -------------   -------------   -------------

# TextLoader => Loads the .txt files and returns a single Document Object in the List
# PyPDFLoader => Loads the pdf and returns a list of Document Object where each Doc Objcet is a single of the pdf
# DirectoryLoader => Loads multiple pdfs and txt files 
# webLoader => loads web pages