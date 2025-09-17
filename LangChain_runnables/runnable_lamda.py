from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser;
from langchain.schema.runnable import RunnableParallel,RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt1= PromptTemplate(
    template='Generate a joke on the topic {topic}',
    input_variables=['topic']
)

parser= StrOutputParser()

generate_joke= prompt1 | model | parser

def word_length(text):
    return len(text.split())


parallel_chain= RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count': RunnableLambda(word_length)
})

final_chain= generate_joke | parallel_chain

response= final_chain.invoke({'topic':'AI'})

print(response['word_count'])
print(response['joke'])
