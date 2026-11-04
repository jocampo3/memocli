import click
from memo.storage import load_memos, write_memos

@click.command()
@click.argument('memo_id', required=False, help='Remove a memo using memo ID.')
def pop(memo_id : str):
    """Remove newest memo or remove using memo ID"""
    data = load_memos()

    if not data["memos"]:
        click.echo('No memos found. Create your first one with "memo add".')
        return

    if memo_id:
        init_count = len(data["memos"])

        data["memos"] = [
            memo for memo in data["memos"]
            if memo.get('id') != memo_id
        ]

        if len(data["memos"]) == init_count:
            click.echo('Memo not found')
            return

        write_memos(data)

        click.echo('Memo removed')
    else:
        data["memos"].pop()

        write_memos(data)

        click.echo('Memo removed')

