# 🏥 MediChat RAG – AI Medical Document Assistant

MediChat RAG is a **Streamlit-based chatbot** that lets users upload medical documents (PDFs) and interact with them using **Retrieval-Augmented Generation (RAG)**.  
It leverages **FAISS** for vector search, **LangChain** for orchestration, and **EuriAI/OpenAI models** for generating context-aware responses.

---

## 🚀 Features
- 📁 Upload multiple medical PDFs  
- 🧩 Automatic text extraction & chunking  
- 🔎 Vector search with FAISS for relevant context  
- 💬 Chat interface powered by Streamlit  
- ⚡ Context-aware answers using LLMs  
- 🎉 Clean, responsive UI with custom styling  

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/medichat-rag.git
   cd medichat-rag


2.Create and activate a virtual environment:

    python3 -m venv rag
    source rag/bin/activate   # Mac/Linux
    rag\Scripts\activate      # Windows

3.Install dependencies:

	  pip install -r requirements.txt

4.Add your API key:
		  Create a .env file in the project root:
		  
		  EURI_API_KEY=your_api_key_here

▶️ Usage

		  Run the Streamlit app:
		  
		  streamlit run main.py

🛠️ Tech Stack

	Python 3.10+
	
	Streamlit
	
	LangChain
	
	FAISS
	
	Sentence-Transformers
	
	EuriAI / OpenAI Models

 medichat-rag/
 
		│── app/
		│   ├── chat_utils.py        # Chat model integration
		│   ├── pdf_utils.py         # PDF text extraction
		│   ├── ui.py                # UI components
		│   ├── vectorstore_utils.py # FAISS index + retrieval
		│   └── config.py            # API key & configs
		│── main.py                  # Streamlit entry point
		│── requirements.txt         # Python dependencies
		│── README.md                # Project documentation
