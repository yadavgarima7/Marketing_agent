import os
import json
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document

load_dotenv()
os.environ["ANONYMIZED_TELEMETRY"] = "False"  # Disable Chroma telemetry

store_path = "memory"
embedding = OpenAIEmbeddings()

# Load captions
with open("posts/hello_recess.json") as f:
    captions = json.load(f)

docs = [Document(page_content=cap["caption"]) for cap in captions]

# Store in vector memory (auto-persisted)
db = Chroma.from_documents(docs, embedding, persist_directory=store_path)
print("✅ Competitor posts ingested into memory.")