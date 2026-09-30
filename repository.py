import subprocess
from pathlib import Path


def clone_repository(
    repo_url: str, destination: Path
) -> None:  # 把终端操作用python实现，需要把命令拆成字符串
    destination.parent.mkdir(parents=True, exist_ok=True) # python直接创建 wokrspaces 目录
    command = [
        "git",
        "clone",
        "--depth",
        "1",
        repo_url,
        str(destination),
    ]
    subprocess.run(command, check=True)
