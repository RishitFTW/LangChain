from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
parser= StrOutputParser()
model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

url='https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2'
loader=WebBaseLoader(url)
docs= loader.load()

content= docs[0].page_content

prompt=PromptTemplate(
    template='What is the product in the content \n {content}',
    input_variables=['content']
)

chain= prompt | model | parser
response= chain.invoke({'content':content})

print(response)