#!/bin/bash

# Set repo directory name (adjust if needed)
SCRIPT_NAME="reminder.py"  # Replace with your actual script name

# Create the workflow directory if it doesn't exist
mkdir -p ".github/workflows"

# Create the workflow YAML file
cat > ".github/workflows/cron-job.yml" <<EOF
name: Scheduled Job

on:
  schedule:
    - cron: "0 * * * *"  # Every hour
  workflow_dispatch:      # Optional: allow manual trigger

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies (optional)
        run: |
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Run the script
        run: python3 $SCRIPT_NAME
EOF

echo "✅ GitHub Actions CRON job created at:"
echo "$REPO_DIR/.github/workflows/cron-job.yml"

