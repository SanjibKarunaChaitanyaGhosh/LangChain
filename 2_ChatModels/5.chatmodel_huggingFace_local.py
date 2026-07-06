from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

import os

os.environ['hf_home']='D:/huggingface_cache' # set the huggingface cache directory to D:/huggingface

# do not run this code, it will not work because,it will dowload the model from huggingface hub, and it will take a lot of time to download the model, and it will also take a lot of space in your local machine. So, it is better to use the model from huggingface endpoint, which is already hosted on huggingface hub.



LLM = HuggingFacePipeline.from_model_id(
    model_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation",
    model_kwargs={"temperature": 0.3, "max_new_tokens": 20}
)
# model = ChatHuggingFace(llm=LLM)            