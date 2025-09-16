from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-flash')



while True:
    user_input= input("You: ")
    if user_input=="exit":
        break
    response= model.invoke(user_input)
    print("AI: ", response.content)


# Now the problem here is the Ai doesnt hold any previous context or chat. so need to store the whole convertation and then invoke so the context 
# remains relevant

history=[]

while True:
    user_input= input("You: ")
    if user_input=="exit":
        break
    history.append(user_input)    
    response= model.invoke(history)
    history.append(response.content)
    print("AI: ", response.content)

# still a problem we are storing the messages as it as NO user,Ai message identification LangChain has builtin classes to fix this issue
# There are three type of msgs in LC system,human,ai
# humanMessage= THe user msg
# systemMessage= The initial msg that we provide to llm like "You are an expert Competitive Programmer blah blah"
# aiMessage= The ai response