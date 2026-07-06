from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

LLM = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation",
    temperature=0.3,
    max_new_tokens=20
)
model=ChatHuggingFace(llm=LLM)

result=model.invoke("What is the capital of India?")
# print(result)
print(result.content)
