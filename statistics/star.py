# -*- coding: utf-8 -*-
# @Time    : 2024/5/8 12:04
# @Author  : 郭志航
# @Site    : https://blog.lingkongstudy.com.cn
# @File    : star.py
# @Software: PyCharm 
# @Comment : acwwt

import json
import requests

# 定义变量
uid = 'InternLM'
repo_list = []
page_id = 1

# 循环获取用户的所有仓库
while True:
    # 拼接url
    url = 'https://api.github.com/users/{}/repos?page={}'.format(uid, page_id)
    # 发送请求
    r = requests.get(url)
    # 将响应转换为字典
    repo_array = json.loads(r.content.decode('utf-8'))
    # 如果响应为空，则结束循环
    if len(repo_array) == 0:
        break
    # 遍历仓库，将不为空的仓库添加到列表中
    for repo in repo_array:
        if not repo['fork']:
            repo_list.append([repo['name'], repo['stargazers_count'], repo['forks_count']])
    # 页面id加1
    page_id += 1

# 排序
repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)

print('=' * 55)
print('\n'.join(['{: <40}★ {: <10}\tfork {} '.format(*repo) for repo in repo_list]))
print('=' * 55)
print('{: <40}★ {: <10}\tfork {} '.format('total', sum([i[1] for i in repo_list]), sum([i[2] for i in repo_list])))
