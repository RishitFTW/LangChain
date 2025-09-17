from langchain_huggingface import HuggingFaceEmbeddings

embeddings= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
response=embeddings.embed_query("Hi Rishit this side")
print(str(response))