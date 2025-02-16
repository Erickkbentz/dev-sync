from saiuncli.cli import CLI
from saiuncli.command import Command

from dev_sync import __version__

from dev_sync.commands.bootstrap import bootstrap_handler
from dev_sync.commands.init import init_handler
from dev_sync.commands.sync import sync_handler

def main():
    # Create the CLI
    dev_sync = CLI(
        title="DevSync",
        description="CLI to sync development enviornments across workspaces.",
        version=__version__
    )

    # Create Subcommands with handlers
    init_command = Command(
        name="init",
        description="Initialize a new DevSync configuration based on the current machine.",
        handler=init_handler,
    )
    bootstrap_command = Command(
        name="bootstrap",
        description="Bootstraps a new machine using DevSync given a config.",
        handler=bootstrap_handler,
    )

    sync_command = Command(
        name="sync",
        description="Sync remote DevSync config from local changes.",
        handler=sync_handler
    )
    
    # Add subcommands to CLI
    dev_sync.add_subcommands([
        init_command,
        bootstrap_command,
        sync_command
    ])

    # Execute the CLI
    dev_sync.run()


if __name__ == "__main__":
    main()