#!/bin/bash

set -e

REPO="jocampo3/memocli"
INSTALL_DIR="$HOME/.local/share/memocli"
BIN_DIR="$HOME/.local/bin"
DATA_DIR="$HOME/.memocli"

echo "Installing Memo..."

# Create installation directories
mkdir -p "$INSTALL_DIR" "$BIN_DIR" "$DATA_DIR"

# Create virtual environment
python3 -m venv "$INSTALL_DIR/venv"

# Install Memo from GitHub
"$INSTALL_DIR/venv/bin/pip" install "git+https://github.com/$REPO.git"

# Create executable symlink
ln -sf "$INSTALL_DIR/venv/bin/memo" "$BIN_DIR/memo"

# Initialize memo storage
if [ ! -f "$DATA_DIR/global.json" ]; then
  printf '{\n  "memos": []\n}\n' >"$DATA_DIR/global.json"
fi

echo "Memo installed successfully!"
echo "Run 'memo --help' to get started."

# Check PATH
case ":$PATH:" in
*":$BIN_DIR:"*) ;;
*)
  echo ""
  echo "Add the following to your shell configuration (~/.bashrc or ~/.zshrc):"
  echo 'export PATH="$HOME/.local/bin:$PATH"'
  ;;
esac
