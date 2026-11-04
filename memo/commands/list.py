import click
from memo.storage import load_memos
from datetime import datetime, date

@click.command()
def list():
    """List memos"""
    data = load_memos()
    memos = data["memos"]

    if memos:
        display_formatted_memos(memos)
    else:
        click.echo('No memos found. Create your first one with "memo add".')

def display_formatted_memos(memos):
    memo_groups = {
        "TODAY": [],
        "UPCOMING": [],
        "MISSED": [],
        "NO DATE": []
    }
    today = date.today()

    for memo in memos:
        if memo.get("date"):
            memo_date = datetime.strptime(memo["date"], "%m-%d-%y").date()
            if memo_date == today:
                memo_groups["TODAY"].append(memo)
            elif memo_date > today:
                memo_groups["UPCOMING"].append(memo)
            elif memo_date < today:
                memo_groups["MISSED"].append(memo)
        else:
            memo_groups["NO DATE"].append(memo)

    for k, v in memo_groups.items():
        if len(v) == 0:
            continue

        click.echo(f'{k} {len(v)}')
        for item in v:
            click.echo(f"{(' ' * 2)}{item.get('id')}{(' ' * 2)}{item.get('text')}")
        click.echo()
