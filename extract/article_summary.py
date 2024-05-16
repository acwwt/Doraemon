from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from llms.Intern_LLM import Intern_LLM

def generate_summary(url: str) -> str:
    # 创建WebBaseLoader实例
    loader = WebBaseLoader(url)
    
    # 加载文档
    docs = loader.load()

    prompt_template = """
    简单总结一下以下内容:
    "{text}"
    格式为:本文介绍了.....
    """

    # 创建PromptTemplate实例
    prompt = PromptTemplate.from_template(prompt_template)

    # 创建Intern_LLM实例
    llm = Intern_LLM()

    # 创建LLMChain实例
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # 创建StuffDocumentsChain实例
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")

    # 运行StuffDocumentsChain
    return stuff_chain.run(docs)