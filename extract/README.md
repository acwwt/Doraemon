# DialogueExtractor 
`DialogueExtractor` 用于从小说或其他文本中提取对话。定义一个数据抽取模式（`schema`），将文本分割成小块，并使用 `Intern_LLM` 实例来抽取对话信息。

## 方法
### __init__()
初始化 `DialogueExtractor` 实例，设置文本编码器和定义数据抽取模式。

### define_schema()
创建一个数据抽取模式，指定要提取的对话信息结构。

### read_text(path)
从指定路径读取文本文件内容。

### save_data(data)
将抽取的数据以 JSON 格式保存到文件。

### get_chunk(text)
将长文本分割成小块，每块不超过模型的最大令牌长度。

### run(chains, text)
运行数据抽取链，尝试从文本中抽取对话信息。

### read_dialogue(path)
从输出文件中读取已保存的对话数据。

### extract_dialogue(file)
处理文件，提取对话，并保存结果。

## 使用示例
```python
extractor = DialogueExtractor()
dialogues = extractor.extract_dialogue("path_to_your_text_file.txt")
print(dialogues)