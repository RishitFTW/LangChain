from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# chat template
chat_template=[{
    ('system','You are helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
}]


chat_history=[]
# load chat history
with open('message_history.txt') as f:
    chat_history.extend(f.readlines())

prompt=chat_template.invoke({'chat_history':chat_history, 'query':'where is my refund'})

response=model.invoke(prompt)