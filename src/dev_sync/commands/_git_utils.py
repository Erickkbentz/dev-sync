import subprocess
import os


def _init_git_repo(dir: str):
    if not os.path.exists(os.path.join(dir, ".git")):
        subprocess.run(["git", "init", dir], check=True)
        print(f"✅ Initialized Git repository in `{dir}`")
        return
    print(f"⚠️ Git repository already exists in `{dir}`.")
    return


def _commit_changes(dir: str, message: str = "Initial commit"):
    if not os.path.exists(os.path.join(dir, ".git")):
        print(f"⚠️ No Git repository found in `{dir}`.")
        return

    # if no changes, return
    if not subprocess.run(
        ["git", "status", "--porcelain"], cwd=dir, check=True, stdout=subprocess.PIPE
    ).stdout:
        print(f"⚠️ No changes to commit in `{dir}`.")
        return

    subprocess.run(["git", "add", "."], cwd=dir, check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=dir, check=True)
    print(f"✅ Committed changes in `{dir}`")
    return
