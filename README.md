# ⚡ Local RAG Agent: Offline Q&A & Document Summarizer 🍕🤖

A lightweight, privacy-focused, **100% local RAG (Retrieval-Augmented Generation)** pipeline. Query structured CSV data, extract relevant semantic chunks via vector search, and generate concise summaries using local LLMs—zero cloud APIs, zero subscription fees.

---

## 🚀 Features

* 🔒 **100% Offline & Private:** Runs entirely on local hardware using Ollama. No data ever leaves your machine.
* ⚡ **Vector Search Engine:** Leverages **ChromaDB** with persistent local storage for fast similarity matching.
* 🧠 **Smart Embeddings:** Uses `mxbai-embed-large` to convert text data into dense vector representations.
* 💬 **Local LLM Inference:** Powered by `llama3.2:1b` via **LangChain** for concise extraction and bullet-point summaries.
* 📊 **CSV Data Ingestion:** Reads structured records, processes metadata, and builds searchable document indexes on first boot.

---

## 🛠️ Tech Stack

* **Framework:** [LangChain](https://www.langchain.com/) (`langchain-core`, `langchain-ollama`, `langchain-chroma`)
* **Local Inference:** [Ollama](https://ollama.com/)
* **Vector Store:** [ChromaDB](https://www.trychroma.com/)
* **Data Handling:** [Pandas](https://pandas.pydata.org/)
* **Language:** Python 3.10+

---

## 📂 Project Structure

```text
├── chroma_db/             # Auto-generated persistent vector database
├── story.csv              # Source CSV containing data records & metadata
├── vector.py              # Embedding generation, vector indexing & retriever setup
├── main.py                # Interactive CLI loop & LangChain prompt pipeline
├── requirements.txt       # Python dependencies
└── README.md
