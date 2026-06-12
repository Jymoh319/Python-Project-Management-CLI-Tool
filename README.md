# Project Management Tracker CLI Tool

An enterprise-grade Command-Line Tool built in Python to track structural user allocations, milestones, and task matrices.

##  Installation and Activation Protocol
1. **Initialize Virtual Container Matrix via Pipenv:**

```bash
pipenv install --dev
```

2. **Execute Automated Verification Tests:**

```Bash
pipenv run pytest
```


# Command Execution Examples
## Register a New User:
```Bash
pipenv run python main.py add-user --name "karanja" --email "james@gmail.com"
```

## Bind a New Project:

```Bash
pipenv run python main.py add-project --title "API Gateway" --user "kamwaro" --due "2026-11-20"
```

## Inject a Dependent Task:

```Bash
pipenv run python main.py add-task --project "API Gateway" --title "Configure CORS Policies" --assignee "Alice"
```

## Flag a Task as Complete:

```Bash
pipenv run python main.py complete-task --id "1"
```

## View All Projects:

```Bash
pipenv run python main.py list-projects
```
