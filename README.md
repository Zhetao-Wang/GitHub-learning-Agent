# GitHub 学习 Agent

> 输入一个 GitHub 仓库链接，让 AI 将项目源码整理成一份适合阅读和学习的中文 HTML 文档。

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-MVP-orange)
![License](https://img.shields.io/badge/license-MIT-green)

GitHub 学习 Agent 是一个用于练习工程化 Python 开发的学习项目。它会克隆指定仓库、读取其中的文本文件，将整理后的仓库内容发送给 DeepSeek，最后在本地生成一份带有项目讲解、学习顺序和问答环节的 HTML 学习文档。

当前版本是一个可以完整运行的 MVP（最小可行产品），主要面向可信的公开 GitHub 仓库。

## 目录

- [GitHub 学习 Agent](#github-学习-agent)
  - [目录](#目录)
  - [项目功能](#项目功能)
  - [运行效果](#运行效果)
  - [环境要求](#环境要求)
  - [快速开始](#快速开始)
    - [1. 克隆项目](#1-克隆项目)
    - [2. 创建并激活 Conda 环境](#2-创建并激活-conda-环境)
    - [3. 安装依赖](#3-安装依赖)
    - [4. 创建本地环境变量文件](#4-创建本地环境变量文件)
  - [环境变量](#环境变量)
  - [使用方法](#使用方法)
  - [项目结构](#项目结构)
  - [安全与隐私](#安全与隐私)
  - [参与贡献](#参与贡献)
  - [许可证](#许可证)

## 项目功能

- 接收标准的 GitHub HTTPS 仓库链接。
- 使用浅克隆下载仓库的最新版本。
- 扫描仓库中的文件并读取 UTF-8 文本内容。
- 将仓库内容整理成带有文件路径的上下文。
- 通过 OpenAI Python SDK 调用 DeepSeek API。
- 生成包含项目简介、目录结构、核心模块、运行方式和学习顺序的中文 HTML。
- 自动创建 `output/` 目录并保存生成结果。



## 运行效果

程序运行完成后，会在 `output/` 目录中生成文件：

```text
output/<仓库所有者>-<仓库名称>-study-guide.html
```

例如，分析 `https://github.com/psf/requests` 后，输出文件名将是：

```text
output/psf-requests-study-guide.html
```

生成的 HTML 可以直接使用浏览器打开。项目后续会在这里补充实际截图或演示动画。

## 环境要求

- Python 3.12 或兼容版本
- Git
- Conda（推荐，但不是必须）
- DeepSeek API Key
- 可访问 GitHub 和 DeepSeek API 的网络环境

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Zhetao-Wang/GitHub--Agent.git
cd GitHub--Agent
```

### 2. 创建并激活 Conda 环境

```bash
conda create --name github-study-agent python=3.12
conda activate github-study-agent
```

如果不使用 Conda，也可以使用 Python 自带的虚拟环境工具。

### 3. 安装依赖

```bash
python -m pip install -r requirements.txt
```

### 4. 创建本地环境变量文件

```bash
cp .env.example .env
```

打开 `.env`，填入自己的 DeepSeek API Key：

```dotenv
DEEPSEEK_API_KEY=你的_API_Key
```

不要把真实 API Key 提交到 Git 仓库。项目已经通过 `.gitignore` 忽略 `.env`。

## 环境变量

| 变量名 | 是否必需 | 用途 |
| --- | --- | --- |
| `DEEPSEEK_API_KEY` | 是 | 调用 DeepSeek API 时进行身份验证 |

程序启动时会从项目根目录下的 `.env` 文件加载该变量。

## 使用方法

在项目根目录运行：

```bash
python main.py
```

根据提示输入一个仓库链接：

```text
请输入 GitHub 仓库链接：https://github.com/psf/requests
```

请直接输入纯 URL，不要输入 Markdown 链接格式。程序会依次完成仓库克隆、文件读取、AI 分析和 HTML 保存，并在结束时打印生成文件的位置。

再次分析同名仓库时，如果对应的本地目录已经存在，当前版本会直接使用已有内容，不会自动拉取远端更新。

## 项目结构

```text
GitHub--Agent/
├── .env.example          # 环境变量示例
├── .gitignore            # Git 忽略规则
├── .vscode/
│   └── settings.json     # VS Code 项目级配置
├── config.py             # 加载和校验 API Key
├── context_builder.py    # 组合仓库文件内容
├── deepseek_client.py    # 构造提示词并调用 DeepSeek
├── html_writer.py        # 保存生成的 HTML
├── main.py               # 程序入口和流程编排
├── repository.py         # 克隆 GitHub 仓库
├── scanner.py            # 扫描和读取仓库文件
├── requirements.txt      # Python 依赖版本
└── README.md             # 项目说明文档
```

运行过程中还会生成以下本地目录：

```text
workspaces/               # 存放克隆下来的仓库
output/                   # 存放生成的学习文档
```

这两个目录包含运行时数据，不会提交到 Git 仓库。



## 安全与隐私

仓库文件内容会发送给 DeepSeek API 进行分析。因此：

- 不要使用本项目处理包含密码、Token、个人信息或商业机密的仓库。
- 当前版本建议只分析自己信任的公开仓库。
- 仓库文件属于待分析数据，不应被当作程序指令执行。
- HTML 由模型直接生成，打开未知仓库生成的文件前应先检查其内容。
- `.env` 仅保存在本地，不要提交、截图或分享其中的 API Key。


## 参与贡献

这是一个学习中的项目，欢迎通过 Issue 提出建议，也欢迎提交 Pull Request。

推荐的贡献流程：

1. Fork 本仓库。
2. 创建自己的功能分支。
3. 完成修改并进行本地验证。
4. 提交清晰、单一目的的 commit。
5. 创建 Pull Request，说明修改原因和验证方式。

提交代码前，请确认没有包含 API Key、生成文件、克隆下来的仓库或其他隐私数据。

## 许可证

本项目采用 MIT License。正式的许可文本将保存在项目根目录的 `LICENSE` 文件中。
