#!/bin/bash

# Navigate to the tex directory
cd /home/marcus/Documents/tex

# Get the name of the file that was compiled (passed as argument)
TEX_FILE="$1"

# Add all changes
git add -A

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Create commit message with timestamp and file name
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
if [ -n "$TEX_FILE" ]; then
    COMMIT_MSG="Auto-commit: Compiled $TEX_FILE at $TIMESTAMP"
else
    COMMIT_MSG="Auto-commit: LaTeX compilation at $TIMESTAMP"
fi

# Commit changes
git commit -m "$COMMIT_MSG"

# Push to remote if it exists
if git remote | grep -q origin; then
    git push origin "$(git branch --show-current)" 2>/dev/null || {
        echo "Note: Push failed. You may need to set up the remote or upstream branch."
    }
else
    echo "Note: No remote repository configured. Run 'git remote add origin <url>' to set one up."
fi
