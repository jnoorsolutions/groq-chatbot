import streamlit as st                                      # 🔧 Streamlit for UI
from dotenv import load_dotenv                              # 🔧 load .env into os.environ
import os                                                   # 🔧 interact with environment vars

from langchain_groq import ChatGroq                         # 🔧 Groq LLM integration
from langchain.memory import ConversationBufferMemory       # 🔧 memory backend for chat
from langchain.chains import ConversationChain              # 🔧 chain that wires LLM + memory

# ─── Load API Key ───────────────────────────────────────────────────────────────
load_dotenv()                                               # 📥 read .env file
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")      # 🔑 set Groq key
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

# ─── Streamlit App Setup ────────────────────────────────────────────────────────
st.set_page_config(page_title="Groq Memory Chatbot")        # 🖥️ title in browser tab
st.title("Groq Chatbot with Memory")                       # 🖥️ app header

# ─── Sidebar Controls ───────────────────────────────────────────────────────────
model_name = st.sidebar.selectbox(                          # 🔽 pick a supported model
    "Select Groq Model",
    ["llama3-8b-8192", "deepseek-r1-distill-llama-70b", "gemma2-9b-it"]
)
temperature = st.sidebar.slider(                           # 🎲 randomness
    "Temperature", 0.0, 1.0, 0.7
)
max_tokens = st.sidebar.slider(                            # 📏 max response length
    "Max Tokens", 50, 300, 150
)

# ─── Initialize Memory & History ────────────────────────────────────────────────
if "memory" not in st.session_state:
    # 🔄 persist memory across reruns
    st.session_state.memory = ConversationBufferMemory(
        return_messages=True   # return as list of messages, not one big string
    )

if "history" not in st.session_state:
    # 🗒️ store role/content pairs for display
    st.session_state.history = []

# ─── User Input ─────────────────────────────────────────────────────────────────
user_input = st.chat_input("You:")  # ↩️ widget that clears itself on Enter

if user_input:
    # 📝 append user turn to visible history
    st.session_state.history.append(("user", user_input))

    # 🔄 instantiate a fresh LLM for this turn
    llm = ChatGroq(
        model_name=model_name,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # 🔗 build ConversationChain with our memory
    conv = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )

    # 🤖 get AI response (memory is updated internally)
    ai_response = conv.predict(input=user_input)

    # 📝 append assistant turn to visible history
    st.session_state.history.append(("assistant", ai_response))

# ─── Render Chat Bubbles ────────────────────────────────────────────────────────
for role, text in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(text)         # 🗨️ user style
    else:
        st.chat_message("assistant").write(text)    # 🗨️ assistant style
