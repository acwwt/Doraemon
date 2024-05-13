from openai import OpenAI
import os
from langchain.llms.base import LLM
from typing import Dict, List, Optional, Tuple, Union
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())

api_key = os.environ["STEP_API_KEY"]
 
client = OpenAI(
    api_key=api_key,
    base_url="https://api.stepfun.com/v1",
)

def get_completion(prompt, model="step-1-200k"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # 模型输出的温度系数，控制输出的随机程度
    )

    return response.choices[0].message.content
    

class Step_LLM(LLM):
    model_type: str = "Step"


    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "Step"
    
    def _call(self, prompt: str, history: List = [], stop: Optional[List[str]] = None) -> str:
        res = get_completion(prompt)
        return res
    
    @property
    def _identifying_params(self):
        """Get the identifying parameters.
        """
        _param_dict = {
            "model": self.model_type
        }
        return _param_dict
