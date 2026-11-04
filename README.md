# Memo

A simple CLI tool for managing reminders directly from your terminal.

## Installation

Install Memo by running the following command:

```bash
curl -fsSL https://raw.githubusercontent.com/jocampo3/memocli/main/install.sh | bash
```

If `~/.local/bin` isn't already in your PATH, add the following to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Restart your terminal or reload your shell configuration.

## Commands

| Command | Description |
|---|---|
| `memo add "text" [day]` | Create a memo |
| `memo list` | List memos |
| `memo memo pop [memo_id]` | Remove newest memo or remove using memo ID |

## Storage

Memos are stored locally in `~/.memocli/global.json`.

Your memo data is preserved when Memo is updated or reinstalled.

## Updating

Run the installation command again to install the latest version from GitHub.

## Uninstalling

```bash
rm -rf ~/.local/share/memocli
rm -f ~/.local/bin/memo
```

Your existing memos in `~/.memocli/` are intentionally preserved. To remove them too:

```bash
rm -rf ~/.memocli
```
