import gradio as gr
from dialogue_extractor import DialogueExtractor
from article_summary import generate_summary




def ui_interface(extractor):
    output = gr.JSON()
    extract = gr.Interface(fn=extractor.extract_dialogue, inputs="file", outputs=output, title="Doraemon的对话提取器", description="### 将小说文件上传到上面提交即可，不过当前仅支持txt文件，后续有时间会继续优化支持更多文件格式！")

    summary = gr.Interface(fn=generate_summary, inputs="text", outputs="text", title="Doraemon的总结面包", description="### 输入文章连接，即可获取文章的摘要！")
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        html_code = """
                    <h1 style="text-align: center;"> 💬 Doraemon的口袋 </h1>
                    <div class="container" style="display: flex; flex-wrap: wrap;">
                        <div class="title" style="text-align: center; flex: 1 1 50%; padding: 10px;">
                            <h2> 🎉 目前项目已经在github上面，目标是做成能够方便大家创作大模型应用的多工具类agent。</h2>
                            <h3> 🤖 项目作者：<a href="https://github.com/acwwt">@acwwt</a></h3>
                            <h3> 🧐 项目地址：<a href="https://github.com/acwwt/Doraemon">Doraemon</a></h3>
                            <h3> 📚 项目文档：<a href="https://github.com/acwwt/Doraemon/blob/main/docs/README.md">README</a></h3>
                            <h3> ✨ 项目使用：<a href="https://github.com/InternLM">InternLM</a> api接口提取对话，大家可以给InternLM点个star⭐</h3>
                        </div>
                        <img src="https://oss.lingkongstudy.com.cn/blog/202405131653596.png" alt="Doraemon" style="width:50%; height:50%; border-radius: 20px; flex: 1 1 50%; padding: 10px;">
                    </div>
                    """
        gr.HTML(html_code)
        gr.TabbedInterface(
                          [extract, summary],
                          ["🤖 对话抽取", "🔍 文章摘要"],
                          )
        
    demo.launch()

if __name__ == "__main__":
    extractor = DialogueExtractor()
    ui_interface(extractor)