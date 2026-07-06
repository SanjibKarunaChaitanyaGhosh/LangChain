from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimemsions=300)

documents=[
    'Virat Kohli is a famous Indian cricketer.',
    'Sachin Tendulkar is a legendary Indian cricketer.',
    'Rohit Sharma is a talented Indian cricketer.',
    'MS Dhoni is a former Indian cricketer and captain.',
    'Sourav Ganguly is a former Indian cricketer and captain.',
    'Schin Tendulkar is known as the "God of Cricket" in India.',
    'Rohit Sharma is known for his aggressive batting style.',
    'Jasprit Bumrah is a fast bowler for the Indian cricket team.',
    'mohammed shami is a fast bowler for the Indian cricket team.',
]

query="Tell me about Schin Tendulkar and his achievements in cricket."


doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

cosine_similarity_score=cosine_similarity([query_embedding],doc_embeddings)[0]
# using this 0 we get 1d list instead of 2d list as output

print(sorted(list(enumerate(cosine_similarity_score)),key=lambda x:x[1],reverse=True)[-1])

index,score=sorted(list(enumerate(cosine_similarity_score)),key=lambda x:x[1])[-1]

print(f"Most similar document to the query is: {documents[index]} with a similarity score of {score}")