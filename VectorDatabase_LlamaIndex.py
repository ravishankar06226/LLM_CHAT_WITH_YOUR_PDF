from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_BASE_URL"],
)
models = client.models.list()
print(models)
print(models.data[0].id)



documents = SimpleDirectoryReader("data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

Settings.llm = Ollama(model=models.data[0].id, request_timeout=360.0)

index = VectorStoreIndex.from_documents(documents)

engine = index.as_query_engine()
result = engine.query("What is supervise learning?")
print(result)

index.storage_context.persist("ml_index")

