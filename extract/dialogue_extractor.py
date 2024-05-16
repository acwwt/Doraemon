from llms.Intern_LLM import Intern_LLM
from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text, Number
import tiktoken
import json
import os
from tqdm import tqdm

class DialogueExtractor:
    def __init__(self):
        self.enc = tiktoken.get_encoding("cl100k_base")
        self.schema = self.define_schema()
        
    def define_schema(self):
        return Object(
            id="script",
            description="Schema for extracting dialogues from novels",
            attributes=[
                Text(
                    id="role",
                    description="The role of the character speaking the dialogue",
                ),
                Text(
                    id="dialogue",
                    description="The actual dialogue spoken by the character",
                )
            ],
            examples=[
               (
                '''
                龙王说∶“再也没有比这更重的兵器了。”悟空不信，和龙王吵了起来，龙婆给龙王说∶“大禹治水时，测定海水深浅的神珍铁最近总是放光，就把这给他，管他能不能用，打发他走算了。”龙王听后告诉悟空∶“这宝物太重了，你自己去取吧！”
                ''',
                [
                    {"role": "龙王", "dialogue": "再也没有比这更重的兵器了。"},
                    {"role": "龙婆", "dialogue": "大禹治水时，测定海水深浅的神珍铁最近总是放光，就把这给他，管他能不能用，打发他走算了。”龙王听后告诉悟空∶“这宝物太重了，你自己去取吧！"},
                ],
                ),
                (
                '''
                悟空见八戒这么长时间不回来，就拔根毫毛变成自己，陪着师父和沙僧，真身驾云来到山凹里，见八戒和妖精正在交战，便高声叫道∶“八戒别慌，老孙来了！”八戒一听，来了精神，没几下，就把那群妖怪打败了。
                ''',
                [
                    {"role": "悟空", "dialogue": "八戒别慌，老孙来了！"},
                ],
                )
            ],
            many=True,
        )
    
    def read_text(self, path):
        with open(path, mode='r', encoding='utf-8') as f:
            return f.read()
    
    def save_data(self, data):
        filename = path.split('/')[-1].split('.')[0]
        filepath = f"./output/{filename}.jsonl"
         # 检查文件是否存在，如果不存在则创建
        if not os.path.exists(filepath):
            os.makedirs(os.path.dirname(filepath), exist_ok=True)  # 创建必要文件夹
            open(filepath, 'w').close()  # 创建空文件
        with open(filepath, mode='a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
            
    def get_chunk(self, text):
        """
        text: str
        return: chunk_text
        """
        max_token_len = 600
        chunk_text = []

        curr_len = 0
        curr_chunk = ''

        lines = text.split('\n')  # 假设以换行符分割文本为行

        for line in lines:
            line_len = len(self.enc.encode(line))
            if line_len > max_token_len:
                print('warning line_len = ', line_len)
            if curr_len + line_len <= max_token_len:
                curr_chunk += line
                curr_chunk += '\n'
                curr_len += line_len
                curr_len += 1
            else:
                chunk_text.append(curr_chunk)
                curr_chunk = line
                curr_len = line_len
        
        if curr_chunk:
            chunk_text.append(curr_chunk)
        
        return chunk_text

    def run(self, chains, text):
        max_attempts = 3  # 最大尝试次数
        current_attempt = 1
        while current_attempt < max_attempts:
            try:
                response = chains.run(text)
            except Exception as e:
                print(e)
            else:
                break
            finally:
                print(f"第 {current_attempt} 次尝试完成。")
                current_attempt += 1

        if 'script' in response['data']:
            for item in response['data']['script']:
                # print(item)
                self.save_data(item)
        else:
            pass

    def read_dialogue(self, path):
        # path:字符串形式
        filename = path.split('/')[-1].split('.')[0]
        res = []
        with open(f"./output/{filename}.jsonl", mode='r', encoding='utf-8') as file:
            for line in file.readlines():
                res.append(json.loads(line))
        return res

    def extract_dialogue(self, file):
        llm = Intern_LLM()
        global path
        path = file.name
        chain = create_extraction_chain(llm, self.schema)
        chunk_list = self.get_chunk(self.read_text(path))
        for i in tqdm(range(len(chunk_list))):
            try:
                self.run(chain, chunk_list[i])
            except Exception as e:
                print(e)
        dialogue_list = self.read_dialogue(path)
        return dialogue_list