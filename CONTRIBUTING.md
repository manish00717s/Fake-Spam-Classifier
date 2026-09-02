# Contributing

Thanks for your interest in improving the SMS Spam Classifier project.

## Getting Started

1. Fork and clone the repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Running Tests

The preprocessing pipeline is covered by unit tests:

```bash
python -m pytest tests/ -v
```

Please make sure all tests pass before opening a pull request, and add tests
for any new behavior you introduce.

## Making Changes

- Create a feature branch: `git checkout -b feature/short-description`
- Keep commits focused and write clear commit messages.
- Follow the existing code style (PEP 8 for Python).
- Update documentation when you change behavior.

## Pull Requests

- Describe what changed and why.
- Note how you tested the change.
- Link any related issues.

## Reporting Issues

Open an issue with steps to reproduce, expected vs. actual behavior, and your
environment details (OS, Python version).
