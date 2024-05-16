<div align="center">
<h1 align="center">Hello Doraemon!</h1>
<h3 align="center">
<img alt="Doraemon" src="./images/Doraemon.png" style="width:50%; height:50%; border-radius: 20px;"> 
</h3>

[![license](https://img.shields.io/github/license/acwwt/Doraemon.svg)](https://github.com/acwwt/Doraemon/tree/main/LICENSE)
[![open issues](https://img.shields.io/github/issues-raw/acwwt/Doraemon)](https://github.com/acwwt/Doraemon/issues)
![Visitors](https://api.visitorbadge.io/api/visitors?path=acwwt%2FDoraemon%20&countColor=%23263759&style=flat)
![GitHub forks](https://img.shields.io/github/forks/acwwt/Doraemon)
![GitHub Repo stars](https://img.shields.io/github/stars/acwwt/Doraemon)

<p align="center">
  <a href="https://github.com/acwwt/Doraemon/blob/main/README.md">简体中文</a>
</p>

</div>

## 简介

`Doraemon` 的想法是利用大语言模型的能力，创建更多的工具，将大语言模型能力合理用起来，目前正在开发阶段，现在已经实现了`提取小说对话`的应用实现，后续会部署在线的应用。

后续有想法将大模型嵌入到博客中，构建一个针对个人知识库的总结助手，我暂且命名为`Doraemon-GPT`。

目前，Doraemon 主要包含以下功能：

### 1. 小说对话提取

该工具的灵感来源于[葱佬](https://github.com/KMnO4-zx)huanhuan-chat项目的一个分支extract-dialogue，大家可以去关注一下[huanhuan-chat](https://github.com/KMnO4-zx/huanhuan-chat)点个star⭐。

具体内容可以看[extract](./extract/)，目前默认使用的是InternLM的api接口，因为在我测试过程中，发现InternLM提取对话的能力更好，大家可以给[InternLM](https://github.com/InternLM)点个star⭐。

后面可能会支持其他国产大模型的api，国外的不太方便所以就暂时不考虑了，不过现在项目主要还是使用InternLM的api。后续的话会将`dialogue_extractor`集成到lagent中，就是可以使用本地的InternLM模型进行对话提取。

下面是`dialogue_extractor`的web UI：
<img alt="web-ui" src="./images/ex-1.png" style="border-radius: 8px;"> 


### 2. 大模型-文章总结

后续的话还会将大模型能力嵌入到博客中去，利用大语言模型进行文章的总结，这个灵感来源于Halo博客hao主题的一个功能-TianGPT，大家也可以关注一下我的博客[Mikey](https://blog.lingkongstudy.com.cn/about)，欢迎大家在博客里面评论交流。
<img alt="blog" src="./images/ex-2.png" style="border-radius: 8px;"> 

前段时间也顺手做了两个小工具，一个是github信息统计，另一个是二维码拼接的，项目分别在[GitHub-Repository-Information](https://github.com/acwwt/GitHub-Repository-Information)和[QRC-Processo](https://github.com/acwwt/QRC-Processo)。
同时应用我也部署在了OpenxLab上面了[Github仓库信息](https://openxlab.org.cn/apps/detail/M1key/GitHub-Repository-Information)，[QRC-Processo](https://openxlab.org.cn/apps/detail/M1key/QRC-Processo)。


## 贡献

欢迎大家加入到项目中，大家可以提交issue。

## 许可证

[MIT](https://github.com/acwwt/Doraemon/blob/main/LICENSE)


