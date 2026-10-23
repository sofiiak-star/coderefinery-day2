# CodeRefinery Day 2 starter

A small Python project for the NLTU workshop with Yuriy Paslavskyi.

## Start your own project

1. Select **Use this template → Create a new repository** on GitHub.
2. Create the repository in your own account; include only the default branch.
3. Clone **your new repository** and open its folder in VS Code.

## Run on Windows (PowerShell)

Requires Git and Python 3.13 (Python 3.12 also works for this example).
Run these commands from the repository folder:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest -v example.py
```

The initial checkpoint has **1 passing test**.
Open `example.py` and continue with the instructor.

## Workshop tasks

We will explore tests, branches, pull requests, GitHub Actions, and AI-assisted
project documentation. Expand this short README during the documentation task.

## License and sources

This teaching adaptation is distributed under [MIT](LICENSE).
It follows the learning pattern of [CodeRefinery testing](https://coderefinery.github.io/testing/)
and [full-cycle collaboration](https://coderefinery.github.io/testing/full-cycle-ci/).
Prepared with AI assistance; the local test checkpoints were checked separately.
