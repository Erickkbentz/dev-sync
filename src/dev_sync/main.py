import click

from dev_sync.rich_click import RichCommand, RichGroup
from dev_sync.logging import logger, configure_logging, console

@click.group(
    cls=RichGroup,
    help="DevSync: A state management tool for development environments"
)
def dev_sync():
    configure_logging()
    pass

@dev_sync.command(cls=RichCommand)
@click.option(
    "--git-repo", 
    "-g",
    type=str,
    default="dev-sync-store",
    help="The URL of the git repository to sync with"
)
def init(
    git_repo: str
):
    console.print("Initializing a new DevSync project")

if __name__ == "__main__":
    dev_sync()