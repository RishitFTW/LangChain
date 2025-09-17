from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings=OpenAIEmbeddings(model="text-embeddings-3-large",dimensions=32)
response=embeddings.embed_query("Hello Rishit this side")
print(response)