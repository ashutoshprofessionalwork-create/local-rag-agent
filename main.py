from langchain_ollama import OllamaLLM

from langchain_core.prompts import ChatPromptTemplate

from vector import retriever



model=OllamaLLM(model="llama3.2:1b")



Template=Template = """
You are an expert in summarizing and extracting information from text.

Context:
{TEXT}

Question:
{QUESTIONS}

Based strictly on the provided context above, provide a clear and concise response in bullet points, followed by a one-sentence conclusion. If the answer is not contained in the text, state that clearly.
"""


prompt=ChatPromptTemplate.from_template(Template)



chain=prompt | model

print("\n--------------------------------------")
print("\n--------------------------------------")
ask="summary in detail "
summary=retriever.invoke(ask)
result = chain.invoke(

  {"TEXT": summary, "QUESTIONS": ask}

)
print(result)
print("\n---------------------------------------")
print("---------------------------------------")

#ask="ask user if the user have any query regarding the data with qn mark "
#summary=retriever.invoke(ask)
#result = chain.invoke(

#  {"TEXT": summary, "QUESTIONS": ask}

#)
#print(result)
#print("\n---------------------------------------")
#print("---------------------------------------")

while True:

 
  print("\n---------------------------------------")
  print("---------------------------------------")
  ask=input("keep asking or press q to exit chat  : ")
  if ask=="q":

    break



  summary=retriever.invoke(ask)



  result = chain.invoke(

  {"TEXT": summary, "QUESTIONS": ask}

)

  print(result)

  print("\n-----------------------------------------------")
  print("\n-----------------------------------------------")
