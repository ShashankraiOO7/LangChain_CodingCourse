from langchain_community.utilities import SerpAPIWrapper
from langchain_huggingface import HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Corrected model and tas
model= ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Set up web search
search = SerpAPIWrapper()


# Create prompt
template = PromptTemplate(
    input_variables=["news", "search_results"],
    template="""
You are a helpful assistant. Given the topic "{news}", and the following web search results:

{search_results}

Generate a comprehensive and updated explanation.
"""
)
news = input("Enter the topic on which you want details: ")
results = search.run(news)
print("The New :{}",results)
final_prompt = template.format(news=news, search_results=results)

# Chain
parser = StrOutputParser()
chain = model | parser

# Run
response = chain.invoke(final_prompt)
print(response)
