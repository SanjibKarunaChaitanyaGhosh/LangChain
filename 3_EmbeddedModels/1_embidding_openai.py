from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimension=32)
# dimension 32 is the size of the embiddings vector, you can change 

# we can send a single sentence or a list of sentences to get the embeddings
result=embeddings.embed_query("What is the capital of India ?")


print(str(result))