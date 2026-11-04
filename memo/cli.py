import click
import json
import hashlib
from pathlib import Path
from memo.utils import Date


DATA_DIR = Path.home() / '.memocli'
DATA_FILE = DATA_DIR / 'global.json'

@click.group()
def cli():
    """Memo is a CLI tool used to create memos accessible within your terminal."""
    init()

@cli.command()
def list():
    """List memos"""
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        memos = data["memos"]
 
        if memos:
            for m in memos:
                click.echo(f'{m['id']}: {m['text']}')
        else:
            click.echo('No memos found. Create your first one with "memo add".')

@cli.command()
@click.argument('memo_id', required=False, help='Remove a memo using memo ID.')
def pop(memo_id : str):
    """Remove newest memo or remove using memo ID"""
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

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

        with open(DATA_FILE, 'w') as f:
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        click.echo('Memo removed')
    else:
        data["memos"].pop()

        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)

        click.echo('Memo removed')

@cli.command()
@click.argument('input', help='Create a new memo')
@click.argument('day', required=False, help='Add a date to the memo (Ex: memo add "review PR on" friday)')
def add(input, day : str | None):
    """Create a memo"""
    h = hashlib.sha256()
    h.update(f'{input} {day}'.encode())
    id = h.hexdigest()[:10]

    memo = {
        "id": id,
        "text": input,
    }

    if day:
        date = Date()
        date.validate(day)

        if date.is_valid:
            memo["text"] = f"{input} {day}"
            memo["date"] = date.day
        else:
            click.echo('Invalid date entered. Memo not created')
            return


    with open(DATA_FILE, 'r+') as f:
        data = json.load(f)
        for curr_memo in data["memos"]:
            if curr_memo.get("id") == id:
                click.echo("Memo already exists")
                f.close()
                return

        data["memos"].append(memo)
 
        f.seek(0) # reposition pointer
        json.dump(data, f, indent=2)
        f.truncate()

def init():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        with open(DATA_FILE, 'w') as f:
            json.dump({"memos": []}, f, indent=2)

if __name__ == '__main__':
    cli()
