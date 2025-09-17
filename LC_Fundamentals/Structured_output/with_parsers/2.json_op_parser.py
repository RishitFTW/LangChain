from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
parser= JsonOutputParser()

template= PromptTemplate(
    template="Give me 5 facts about {topic} \n {formal_instructions}",
    input_variables=['topic'],
    partial_variables={'formal_instructions':parser.get_format_instructions()}
)


model= ChatGoogleGenerativeAI(model='gemini-1.5-flash')

chain= template | model | parser
result= chain.invoke({'topic':'Delhi'})
print(result)
