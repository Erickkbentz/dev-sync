from saiuncli.cli import CLI
from saiuncli.option import Option
from saiuncli.command import Command

from dev_sync import __version__
from dev_sync.console import console

from dev_sync.commands.init import init_handler
from dev_sync.commands.sync import sync_handler
from dev_sync.commands.add_secret import add_secret_handler
from dev_sync.commands.add_private_file import add_private_file_handler
from dev_sync.commands.commit import commit_handler
from dev_sync.commands.pull import pull_handler
from dev_sync.commands.clone import clone_handler


def main():
    # Create the CLI
    dev_sync = CLI(
        title="DevSync",
        console=console,
        description="CLI to sync development environments across workspaces.",
        version=__version__,
    )

    # Create Subcommands with handlers
    init_command = Command(
        name="init",
        description="Initialize a new devsync_config.yaml based on the current machine’s environment and settings.",
        handler=init_handler,
        Options=[
            Option(
                flags=["-r", "--git-repo"],
                description="The Git repository to use for syncing. If not provided, a new repository will be created.",
                required=False,
            ),
            Option(
                flags=["-d", "--config-dir"],
                description="The directory to save the configuration file. Defaults to ~/.dev-sync.",
                required=False,
            ),
        ],
    )

    clone_command = Command(
        name="clone",
        description="Clone a devsync_config.yaml from a remote repository.",
        handler=clone_handler,
        options=[
            Option(
                flags=["-r", "--git-repo"],
                description="The Git repository to clone the configuration from.",
                required=True,
            ),
            Option(
                flags=["-d", "--config-dir"],
                description="The directory to save the cloned configuration file. Defaults to ~/.dev-sync.",
                required=False,
            ),
        ],
    )

    commit_command = Command(
        name="commit",
        description="Commit the current devsync_config.yaml (and related metadata) to your Git repository.",
        handler=commit_handler,
    )

    pull_command = Command(
        name="pull",
        description="Pull the latest config from your Git repository.",
        handler=pull_handler,
    )

    sync_command = Command(
        name="sync",
        description="Sync your machine to match the devsync_config.yaml.",
        handler=sync_handler,
    )

    add_secret_command = Command(
        name="add-secret",
        description="Add a new secret to AWS Secrets Manager and update the config file.",
        handler=add_secret_handler,
        options=[
            Option(
                flags=["-n", "--secret-name"],
                description="The name of the secret in Secrets Manager.",
                required=True,
            ),
            Option(
                flags=["-s", "--secret-string"],
                description="The secret string to upload",
                required=False,
            ),
            Option(
                flags=["-f", "--file"],
                description="Path to the file containing the secret to upload.",
                required=False,
            ),
            Option(
                flags=["-p", "--target-path"],
                description="Target path on the machine to save the secret to when syncing.",
                required=False,
            ),
            Option(
                flags=["-e", "--target-env"],
                description="Environment variable name to set the secret to when syncing.",
                required=False,
            ),
        ],
    )

    add_private_file_command = Command(
        name="add-private-file",
        description="Upload a private file or folder to S3 and update the config file.",
        handler=add_private_file_handler,
        Option=[
            Option(
                flags=["-n", "--name"],
                description="The name to reference this private file.",
                required=True,
            ),
            Option(
                flags=["-f", "--file"],
                description="Path to the private file to upload.",
                required=False,
            ),
            Option(
                flags=["-d", "--directory"],
                description="Path to the private directory to upload.",
                required=False,
            ),
            Option(
                flags=["-p", "--target-path"],
                description="Target path on the machine to save the file or folder when syncing.",
                required=True,
            ),
        ],
    )

    # Add subcommands to CLI
    dev_sync.add_subcommands(
        [
            init_command,
            clone_command,
            commit_command,
            pull_command,
            sync_command,
            add_secret_command,
            add_private_file_command,
        ]
    )

    # Execute the CLI
    dev_sync.run()


if __name__ == "__main__":
    main()
