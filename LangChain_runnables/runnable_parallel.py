from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser;
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model1= ChatGoogleGenerativeAI(model='gemini-1.5-flash')

llm= HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model2= ChatHuggingFace(llm=llm)
parser= StrOutputParser()
prompt1= PromptTemplate(
    template="Generate 4 advantages of the topc {topic}"
)

prompt2= PromptTemplate(
    template="Generate 4 disadvantages of the topc {topic}"
)

chain1 = RunnableParallel({
    'adv': prompt1 | model1 | parser,
    'disadv':prompt2 | model2 | parser
})

response= chain1.invoke({'topic':'AI'})
print(response['adv'])
print(response['disadv'])
