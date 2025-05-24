import os
import yaml

from dev_sync.commands._git_utils import _init_git_repo, _commit_changes

CONFIG_BASE_DIRECTORY = os.path.expanduser("~/.dev-sync")


def _create_config_dir(config_dir: str):
    if not os.path.exists(config_dir):
        os.makedirs(config_dir, exist_ok=True)
        print(f"✅ Created configuration directory `{config_dir}`")
        return
    print(f"⚠️ Configuration directory `{config_dir}` already exists.")
    return


def _create_config_file(config_dir: str):
    config_file = os.path.join(config_dir, "config.yaml")
    if not os.path.exists(config_file):
        with open(config_file, "w") as f:
            yaml.dump({"name": os.path.basename(config_dir), "configs": []}, f)
        print(f"✅ Created configuration file in `{config_file}`")
        return
    print(f"⚠️ Configuration file already exists in `{config_file}`.")
    return


def init_handler(name: str):
    config_dir = os.path.join(CONFIG_BASE_DIRECTORY, name)
    _create_config_dir(config_dir)
    _create_config_file(config_dir)
    _init_git_repo(config_dir)
    _commit_changes(config_dir)

    print(f"✅ Configuration `{name}` initialized.")
    return
