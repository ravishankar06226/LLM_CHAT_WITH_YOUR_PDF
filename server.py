from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from llama_index.core import Settings, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
from openai import OpenAI
from dotenv import load_dotenv

class Item(BaseModel):
    question:str

load_dotenv()


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)
models = client.models.list()

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

Settings.llm = Ollama(model=models.data[0].id, request_timeout=360.0)

storage_context=StorageContext.from_defaults(persist_dir="ml_index")
index=load_index_from_storage(storage_context)

engine = index.as_query_engine()

result = engine.query("What are the strength of R over Python?")
print(result)

app=FastAPI()

@app.post("/")
async def query(item:Item):
    result = engine.query(item.question)
    return(result)

if __name__ == "__main__":
    uvicorn.run("server:app", host ="127.0.0.1",port=8000)


