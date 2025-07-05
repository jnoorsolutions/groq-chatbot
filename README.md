
# 🤖 Groq Chatbot with Memory – Streamlit App

This is a simple **chatbot application** built using:
- 🧠 [LangChain](https://python.langchain.com)
- ⚡ [Groq LLMs](https://groq.com/)
- 🌐 [Streamlit](https://streamlit.io)
- 🧠 Memory support using `ConversationBufferMemory`

---

## 🚀 Features

✅ Chat with powerful Groq LLMs  
✅ Persistent memory across conversation  
✅ Streamlit UI with chat bubbles  
✅ Sidebar options for model, temperature, and token limits  
✅ Easily deployable on **Streamlit Cloud** or any VPS

---

## 📁 Project Structure

```
.
├── main_chat.py                       # Main Streamlit app
├── requirements.txt             # Python dependencies
├── .streamlit/
│   └── secrets.toml             # Secure API key storage (do not commit)
└── README.md
```

---

## 🧑‍💻 How to Run Locally

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/groq-chatbot.git
cd groq-chatbot
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set API Key

Create `.streamlit/secrets.toml` file:

```toml
GROQ_API_KEY = "your-groq-api-key"
```

### 5️⃣ Run the App

```bash
streamlit run app.py
```

App will run at: [http://localhost:8501](http://localhost:8501)

---

## 🌍 Deployment (Streamlit Cloud)

1. Push this repo to GitHub
2. Go to: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click “New App” and link your GitHub repo
4. After deployment, add your secret:

**In Streamlit Cloud → App Settings → Secrets**
```
GROQ_API_KEY = your-real-groq-api-key
```

---

## 📌 Sidebar Options

| Option       | Description                            |
|--------------|----------------------------------------|
| Model        | Choose between llama3, gemma2, etc.    |
| Temperature  | Controls creativity of response        |
| Max Tokens   | Max length of LLM output               |

---

## 📦 Requirements

📄 `requirements.txt`:
```txt
streamlit
python-dotenv
langchain
langchain-groq
```

---

## 🛡️ Security Tip

**Never commit `.streamlit/secrets.toml` or API keys into GitHub!**

Add this to `.gitignore`:
```
.streamlit/secrets.toml
.env
```

---

## 👨‍💻 Credits

Developed by [JnoorSolutions]  
Powered by: Streamlit + Langchain + Groq

---

## 📄 License

This project is licensed under the MIT License.
