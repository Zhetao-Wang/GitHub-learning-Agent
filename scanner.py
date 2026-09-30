from pathlib import Path


def list_repository_files(repo_path: Path) -> list[Path]:
    files = [
        item.relative_to(repo_path) for item in repo_path.rglob("*") if item.is_file()
    ]  # 返回相对目录
    return files


def read_repository_file(repo_path: Path, relative_path: Path) -> str:
    file_path = repo_path / relative_path

    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(f"无法按 UTF-8 文本读取文件：{relative_path}") from error
