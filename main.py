from pathlib import Path
from urllib.parse import urlsplit

from context_builder import build_repository_context
from deepseek_client import generate_study_html
from html_writer import save_html
from repository import clone_repository


repo_url = input("请输入 GitHub 仓库链接：")

parsed_url = urlsplit(repo_url)

if parsed_url.scheme == "https" and parsed_url.netloc.lower() == "github.com":
    print("协议和网站符合要求")
    parts = parsed_url.path.strip("/").split("/")

    if len(parts) != 2 or not all(parts):
        print("链接路径应包含仓库所有者和仓库名称")
    else:
        owner, repo = parts
        repo = repo.removesuffix(".git")
        destination = Path("workspaces") / repo  #等价于Path（"workspaces", repo）
        
        if destination.exists():
            print("仓库已经存在，将直接使用")
        else: 
            clone_repository(repo_url, destination)
        
        repository_context = build_repository_context(destination)
        print(len(repository_context))

        html = generate_study_html(repository_context)   
        output = Path("output")/f"{owner}-{repo}-study-guide.html"

        saved_html_path = save_html(html, output)

        print(f"学习文档已经生成：{saved_html_path}")


else:
    print("请输入 https://github.com 开头的仓库链接")


