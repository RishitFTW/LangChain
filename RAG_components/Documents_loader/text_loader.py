from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser;
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

loader=TextLoader('cricket.txt',encoding='utf-8')
docs= loader.load()

model=ChatGoogleGenerativeAI(
    model='gemini-1.5-flash'
)

parser= StrOutputParser()

prompt=PromptTemplate(
    template="Summarize the text {text}",
    input_variables=['text']
)

chain= prompt | model | parser

response= chain.invoke({'text':docs[0].page_content})
print(response)
