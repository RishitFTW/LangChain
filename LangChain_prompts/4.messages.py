from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-flash')

history=[
    SystemMessage(content='You are helpful assistant')
]

while True:
    user_input=input('You: ')
    if user_input=="exit":
        break
    history.append(HumanMessage(content=user_input))
    response=model.invoke(history)
    history.append(AIMessage(content=response.content))
    print(response.content)

print(history)