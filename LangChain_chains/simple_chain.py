from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

parser= StrOutputParser()

template= PromptTemplate(
    template='Generate 5 facts about {topic}',
    input_variables=['topic']
)

chain= template | model | parser
response= chain.invoke({'topic':'cricket'})

print(response)