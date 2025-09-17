from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser;
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain.schema.runnable import RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
model= ChatGoogleGenerativeAI(model='gemini-1.5-flash')
parser= StrOutputParser()

prompt1= PromptTemplate(
    template='Generate a joke about the topic about {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Tell me the meaning of the joke {joke}'
)

generate_joke= prompt1 | model | parser

parallel_chain= RunnableParallel({
    'joke': RunnablePassthrough(),
    'exp': prompt2 | model | parser
})

final_chain= generate_joke | parallel_chain

response= final_chain.invoke({'topic':'AI'})

print(response['joke'])
print(response['exp'])
