import click
from memo.storage import init
from memo.commands.list import list
from memo.commands.add import add
from memo.commands.pop import pop
# from memo.commands.search import search


@click.group()
def cli():
    """Memo is a CLI tool used to create memos accessible within your terminal."""
    init()

cli.add_command(list)
cli.add_command(add)
cli.add_command(pop)
# cli.add_command(search)

if __name__ == '__main__':
    cli()
