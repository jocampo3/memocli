import click
from memo.storage import load_memos
from fuzzyfinder import fuzzyfinder

@click.command()
@click.argument("query", required=True, help="Search through your memos using string query")
def search(query):
    """Search memos"""
    data = load_memos()
    memos = data["memos"]
 
    if not memos:
        click.echo('No memos found. Create your first one with "memo add".')
        return

    memo_lookup = { memo["text"]: memo for memo in memos }

    suggestions = list(fuzzyfinder(query, memo_lookup.keys()))

    if not suggestions:
        click.echo("No matches found. Try using a different query.")
        return

    click.echo("RESULTS")
    for suggestion in suggestions:
        memo = memo_lookup[suggestion]
        click.echo(f"{(' ' * 2)}{memo.get('id')}{(' ' * 2)}{memo.get('text')}")
