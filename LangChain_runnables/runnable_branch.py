from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser;
from langchain.schema.runnable import RunnableParallel,RunnableBranch,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt1= PromptTemplate(
    template='Generate a article on the topic {topic}',
    input_variables='topic'
)

parser= StrOutputParser()

generate_joke= prompt1 | model | parser

prompt1= PromptTemplate(
    template='Summarize the folllowing text \n {topic}',
    input_variables='topic'
)

conditional_branch= RunnableBranch(
    (lambda x:len(x.split())>500, prompt1 | model | parser),
    RunnablePassthrough()
)

final_chain= generate_joke | conditional_branch
response= final_chain.invoke({'topic':'AI'})
print(response)