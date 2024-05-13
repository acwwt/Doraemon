import json
import requests
import gradio as gr

def get_repo_info(uid):
    repo_list = []
    page_id = 1
    total_stars = 0
    total_forks = 0

    while True:
        url = f'https://api.github.com/users/{uid}/repos?page={page_id}'
        r = requests.get(url)
        repo_array = json.loads(r.content.decode('utf-8'))

        if not repo_array:
            break

        for repo in repo_array:
            if not repo['fork']:
                repo_list.append({
                    'name': repo['name'],
                    'stargazers_count': repo['stargazers_count'],
                    'forks_count': repo['forks_count']
                })
                total_stars += repo['stargazers_count']
                total_forks += repo['forks_count']

        page_id += 1

    repo_list = sorted(repo_list, key=lambda x: x['stargazers_count'], reverse=True)

    # 格式化输出
    output = "GitHub Repository Information\n"
    output += "Where ⭐ stands for star and 🔧 stands for forks\n"
    output += "=" * 80 + "\n"  # 标题下划线
    for repo in repo_list:
        output += f"{repo['name']:<40} ⭐{repo['stargazers_count']:<10} 🔧{repo['forks_count']}\n"
    output += "=" * 80 + "\n"  # 分隔线
    output += f"Total repositories: 📕{len(repo_list)}\n"
    output += f"Total stars: ⭐{total_stars}\n"
    output += f"Total forks: 🔧{total_forks}\n"

    return output

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 💬 GitHub Repository Information ")
    gr.Markdown("## 🚀 Enter a GitHub username to get their repository information sorted by stars. ")
    gr.Markdown("### 💪 Power by [InternLM](https://github.com/InternLM), If you like, please click a little ⭐ . ")
    gr.Interface(
        fn=get_repo_info,
        inputs="text",
        outputs="text",
        examples=[["InternLM"]]
    )

demo.launch()