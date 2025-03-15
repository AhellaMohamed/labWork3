from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.documents import Document

# Define the model 
llm = ChatGroq(model_name="mixtral-8x7b-32768", api_key="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")

# Define a prompt
prompt = PromptTemplate(
    input_variables=["content", "summary_format"],
    template="Summarize the following article in {summary_format} format:\n\n{content}"
)

# Initialize the chain
chain = LLMChain(llm=llm, prompt=prompt)

def summarize_article(article_content, summary_format):
    """Summarize an article using LangChain."""
    if not isinstance(article_content, str):
        raise ValueError("article_content must be a string")
    
    return chain.invoke({"content": article_content, "summary_format": summary_format})
