from dotenv import load_dotenv
import os

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Load environment
load_dotenv()
os.environ["ANONYMIZED_TELEMETRY"] = "False"

# Load brand profile
with open("brand_profile.txt", "r") as f:
    brand_voice = f.read()

# Set up vector store
store_path = "memory"
embedding = OpenAIEmbeddings()
retriever = Chroma(persist_directory=store_path, embedding_function=embedding).as_retriever()

# Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4", temperature=0.7),
    retriever=retriever
)