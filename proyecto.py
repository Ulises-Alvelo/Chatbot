# import streamlit as st
# from groq import Groq

# # Add name to the page and icon
# st.set_page_config(page_title="AI chat", page_icon="./media/AIchat.png", layout="centered")
# # page title
# st.title("Mi first st app")
# # text input
# name = st.text_input("What's your name?")
# # greetings button
# if (st.button("Hi")):
#     st.write(f"Hi {name}, Welcome to this chatbot")
# models = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']
# def setupPage():
#     #aad title to the page
#     st.title("My AI chat")
#     st.sidebar.title("AI settings") #sidebar creation
#     chooseModel = st.sidebar.selectbox("Please, choose a model", options= models, index=0)
#     return chooseModel

# # 7th class
# def createGroqUser():
#     key = st.secrets["API_KEY"]
#     return Groq(api_key=key)
# def setupModel (client, model, entryMsj):
#     return client.chat.completions.create(
#         model= model,   
#         messages = [{"role": "user", "content": entryMsj}],
#         stream = True
#     )
# def initializeState():
#     if "messages" not in st.session_state:
#         st.session_state.messages=[]

# def showHistory():
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"], avatar=message["avatar"]):
#             st.markdown(message["content"])
# def chatArea():
#     chatContainer = st.container(height=400, border=True)
#     with chatContainer:
#         showHistory()
# def updateHistory(role, content, avatar):
#     st.session_state.messages.append(
#     {"role":role, 
#     "content":content, 
#     "avatar":avatar
#     })

# # model = setupPage()
# # userClient = createGroqUser()
# # initializeState()
# # chatArea()
# # message = st.chat_input("Write a message")
# # if message:
# #     updateHistory("user", message, "🧑🏻‍💻")
# #     entireChat = setupModel(userClient, model, message)
# #     updateHistory("assistant", entireChat, "🤖")
# #     st.rerun()

# #Class 9, functions
# #Chat completo es la caja que almacena el chatbot la respuesta que me da a mi como usuario
# #The complete chat is a box who saves the chatbot, the answer who gives me like a user
# def generate_answer(complete_chat):
#     complete_answer = ""
#     for phrase in complete_chat:
#         if phrase.choices[0].delta.content:
#             complete_answer += phrase.choise[0].delta.content
#             yield phrase.choices[0].delta.content
#         return complete_answer
    
# def main():
#     model = setupPage()
#     userClient = createGroqUser()
#     initializeState()
#     chatArea() #funcion de esta clase
#     message = st.chat_input("Please, write a message")
#     if message:
#         updateHistory("user",message,"🧑🏻‍💻")
#         entireChat = setupModel(userClient, model, message)

#         if entireChat:
#             with st.chat_message("assistant"):
#                 complete_answer = st.write_stream(generate_answer(entireChat))
#                 updateHistory("assistant", complete_answer, "🤖")

#                 st.rerun()

#             [theme]
# primaryColor="fd4b4b"
# backgroundColor="#ffc689"
# secondaryBackgroundColor="fdb466"
# textColor="371d01"
# font="sans serif"




















import streamlit as st
from groq import Groq

# Add name to the page and icon
st.set_page_config(page_title="AI chat", page_icon="./media/AIchat.png", layout="centered")
# page title
st.title("Mi first st app")
# text input
name = st.text_input("What's your name?")
# greetings button
if (st.button("Hi")):
    st.write(f"Hi {name}, Welcome to this chatbot")
models = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']
def setupPage():
    #aad title to the page
    st.title("My AI chat")
    st.sidebar.title("AI settings") #sidebar creation
    chooseModel = st.sidebar.selectbox("Please, choose a model", options= models, index=0)
    return chooseModel

# 7th class
def createGroqUser():
    key = st.secrets["key"]
    return Groq(api_key=key)
def setupModel (client, model, entryMsj):
    return client.chat.completions.create(
        model= model,
        messages = [{"role": "user", "content": entryMsj}],
        stream = True
    )
def initializeState():
    if "messages" not in st.session_state:
        st.session_state.messages=[]

def updateHistory(role, content, avatar):
    st.session_state.messages.append(
    {"role":role, 
    "content":content, 
    "avatar":avatar
    })
def showHistory():
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message["avatar"]):
            st.markdown(message["content"])
def chatArea():
    chatContainer = st.container(height=400, border=True)
    with chatContainer:
        showHistory()
# 
#Hasta aca el codigo funciona





def generate_answer(complete_chat):
    complete_answer = ""
    for phrase in complete_chat:
        if phrase.choices[0].delta.content:
            complete_answer += phrase.choices[0].delta.content
            yield phrase.choices[0].delta.content
    return complete_answer
    
def main():
    model = setupPage()
    userClient = createGroqUser()
    initializeState()
    chatArea() #funcion de esta clase
    message = st.chat_input("Please, write a message")
    if message:
        updateHistory("user",message,"🧑🏻‍💻")
        complete_chat = setupModel(userClient, model, message) #

        if complete_chat: # y cual más?
            with st.chat_message("assistant"):
                complete_answer = st.write_stream(generate_answer(complete_chat))
                updateHistory("assistant", complete_answer, "🤖")

                st.rerun()

if __name__ == "__main__":
    main()