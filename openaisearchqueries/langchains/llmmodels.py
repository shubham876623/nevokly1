import os
os.environ["OPENAI_API_KEY"] = ""


from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from langchain.chains import LLMChain

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


def llminput():


    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",)
    chain = LLMChain(llm=llm, prompt=prompt)

    chain.run("colorful socks")
        
    with open('shakespeare.rtf',encoding='utf-8') as f:
        lines = f.readlines()
    with open('shakespeare.rtf', 'w',encoding='utf-8') as f:
        f.write(str(lines))    
    loader = TextLoader("shakespeare.rtf") 
    
    
    
    
    index = VectorstoreIndexCreator().from_loaders([loader])
    # print(type(index),index)
    
    
    
    
    
    return index