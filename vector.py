from langchain_ollama import OllamaEmbeddings #Import OllamaEmbeddings to convert raw text into numerical vector embeddings using a local Ollama model

from langchain_chroma import Chroma #import chrome -> manage local vectors and querying embeddings

from langchain_core.documents import Document

from pathlib import Path

import os

import pandas as pd # to read csv file



df = pd.read_csv("story.csv")



embedding=OllamaEmbeddings(model="mxbai-embed-large")

add_document=not os.path.exists(db_location)



if add_document:

  documents=[]

  ids=[]



  for i,row in df.iterrows():

    document=Document(

      page_content=row["TITLE"]+" "+row["Review"],metadata={"rating":row["Rating"],"date":row["Date"]},

      id=str(i)

    )

    ids.append(str(i))

    documents.append(document)



vector_store=Chroma(

  collection_name="summary",

  persist_directory=db_location,

  embedding_function=embedding

)



if add_document:

  vector_store.add_documents(documents=documents,ids=ids)
retriever=vector_store.as_retriever(

  search_kwargs={"k":5}

)