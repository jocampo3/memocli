import click
from memo.storage import load_memos, write_memos
import hashlib
from memo.utils import Date

@click.command()
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

    data = load_memos()

    if day:
        date = Date()
        date.validate(day)

        if date.is_valid:
            memo["text"] = f"{input} {day}"
            memo["date"] = date.day
        else:
            click.echo('Invalid date entered. Memo not created')
            return

    for curr_memo in data["memos"]:
        if curr_memo.get("id") == id:
            click.echo("Memo already exists")
            return

    data["memos"].append(memo)

    write_memos(data)

    click.echo('Memo added')
