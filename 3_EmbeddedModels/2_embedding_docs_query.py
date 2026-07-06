from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",dimension=32)
# dimension 32 is the size of the embiddings vector, you can change

documents=[
    'Delhi is the capital of India.',
    'Mumbai is the capital of Maharashtra.',
    'Kolkata is the capital of West Bengal.',
    'Chennai is the capital of Tamil Nadu.',
    'Bangalore is the capital of Karnataka.',
    'Hyderabad is the capital of Telangana.',
    'Jaipur is the capital of Rajasthan.',
    'Lucknow is the capital of Uttar Pradesh.',
    'Bhopal is the capital of Madhya Pradesh.',
    'Patna is the capital of Bihar.',
    'Thiruvananthapuram is the capital of Kerala.',
    'Bhubaneswar is the capital of Odisha.',
]

# we can send a single sentence or a list of sentences to get the embeddings
result=embeddings.embed_documents(documents)


print(str(result))