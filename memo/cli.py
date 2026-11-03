import click
import json
import hashlib
from pathlib import Path


DATA_DIR = Path.home() / '.memocli'
DATA_FILE = DATA_DIR / 'global.json'

@click.group()
def cli():
    """Memo is a CLI tool used to create reminders within your terminal."""
    init()

@cli.command()
def list():
    """Lists current memos"""
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        memos = data["memos"]
        if memos:
            for m in memos:
                click.echo(f'{m['id']}: {m['text']}')
        else:
            click.echo('No memos created. Create your first one with python app.py add')

@cli.command()
@click.argument('memo_id', help='Removes recently created memo')
def rm(memo_id):
    """Removes memo by ID"""
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    if not data["memos"]:
        click.echo('No memos created. Create your first one with python app.py add')
        return

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

@cli.command()
def pop():
    """Removes the most recently created memo"""
    with open(DATA_FILE, 'r+') as f:
        data = json.load(f)
        if not data["memos"]:
            click.echo('No memos created. Create your first one with python app.py add')
            return
        data["memos"].pop()
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

    click.echo('Memo removed')

@cli.command()
@click.argument('input', help='Appends a new memo to memos')
def add(input):
    """Adds new memo"""
    h = hashlib.sha256()
    h.update(f'{input}'.encode())
    id = h.hexdigest()[:10]

    memo = {
        "id": id,
        "text": input
    }

    """Creates a new memo"""
    with open(DATA_FILE, 'r+') as f:
        data = json.load(f)
        data["memos"].append(memo)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

def init():
    DATA_DIR.mkdir(exist_ok=True)

    if not DATA_FILE.exists():
        with open(DATA_FILE, 'w') as f:
            json.dump({"memos": []}, f, indent=2)

if __name__ == '__main__':
    cli()
