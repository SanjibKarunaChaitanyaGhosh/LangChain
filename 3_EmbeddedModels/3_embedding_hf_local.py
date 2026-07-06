from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

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

# vector=embedding.embed_query(documents)
vector=embedding.embed_documents(documents)

print(str(vector))

