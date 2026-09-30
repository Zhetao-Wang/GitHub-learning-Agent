from pathlib import Path

from scanner import list_repository_files, read_repository_file

max_context=16000000

def build_repository_context(repo_path: Path) -> str:
    sections: list[str] = []

    for relative_path in sorted(list_repository_files(repo_path)):
        if ".git" in relative_path.parts:
            continue

        header = f"===== FILE: {relative_path} ====="

        try:
            content = read_repository_file(repo_path, relative_path)
        except ValueError:
            sections.append(f"{header}\n[无法作为 UTF-8 文本读取，已省略文件内容]")
            continue

        sections.append(f"{header}\n{content}")

    if not sections:
        raise RuntimeError("仓库中没有可以整理的文件")
    context = "\n\n".join(sections)
    if len(context) > max_context:
        raise ValueError(f"允许字符数{max_context},实际字符数{len(context)}")
    
    return context
        
