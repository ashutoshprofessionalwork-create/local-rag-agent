# Local RAG Assistant with LangChain, Ollama & ChromaDB

A lightweight, 100% offline Retrieval-Augmented Generation (RAG) pipeline in Python. It indexes structured review data from a local CSV file into ChromaDB using local vector embeddings, then queries an offline LLM via Ollama to answer questions based strictly on the retrieved context.

---

## Features

* **Fully Offline & Private:** Runs entirely on local hardware with zero API keys or cloud services required.
* **Vector Semantic Search:** Uses `mxbai-embed-large` embeddings stored persistently in ChromaDB.
* **Local LLM Inference:** Answers natural language queries using `llama3.2:1b` through Ollama.
* **Deterministic Responses:** Structured prompt chaining ensures the model grounds its answers directly in retrieved context without hallucinations.

---

## Tech Stack

* **Framework:** LangChain (`langchain-core`, `langchain-ollama`, `langchain-chroma`)
* **Vector Store:** ChromaDB
* **LLM & Embeddings:** Ollama (`llama3.2:1b`, `mxbai-embed-large`)
* **Data Processing:** Pandas

---

## Project Structure
