from langchain_ollama import OllamaLLM

from langchain_core.prompts import ChatPromptTemplate

from vector import retriever



model=OllamaLLM(model="llama3.2:1b")



Template="""

You are an expert in summarizing text. given a text {TEXT}, you will provide a concise summary of the main points and key information. Please ensure that the summary is clear, accurate, and captures the essence of the original text.

the summary should be in bullet points format, highlighting the most important aspects of the text. Avoid including unnecessary details or personal opinions. The summary should be easy to read and understand, providing a quick overview of the content.

also add a conclusion sentence that encapsulates the overall message of the text.

Here is the questions to answer: {QUESTIONS}

"""



prompt=ChatPromptTemplate.from_template(Template)



chain=prompt | model



while True:

 

  ask=input("anything you want (press q to quit ) :")

  if ask=="q":

    break



  reviews=retriever.invoke(ask)



  result = chain.invoke(

  {"TEXT": reviews, "QUESTIONS": ask}

)

  print(result)

  print("\n-----------------------------------------------")

  print("\n-----------------------------------------------")

