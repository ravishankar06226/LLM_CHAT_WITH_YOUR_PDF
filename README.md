# LLM_CHAT_WITH_YOUR_PDF

## Create environment and install requirement packages
conda env create -f environment.yml -n LLM_CHAT_WITH_YOUR_PDF

conda activate LLM_CHAT_WITH_YOUR_PDF

## Create a running instence of official ollama docker image
sh run_ollama.sh 

## pull the llama3:8b model
docker exec -it ollama ollama run gemma2:2b

## Test your model
python model_test.py  

## Create VectorDatabase and test query against query
python3 VectorDatabase_LlamaIndex.py

## Create a FastAPI endpoint (API) , can be used later to accept http request
python server.py

## Send request to API and get response
python3 client.py

## Run webapp
python app.py

![image](https://github.com/user-attachments/assets/d450029a-1b68-47ac-a6fd-1403e7d37462)
