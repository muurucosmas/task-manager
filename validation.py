from datetime import datetime

def validate_task_title(title):
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters.")
    return title

def validate_task_description(description):
    if len(description) < 5:
        raise ValueError("Description too short.")
    
    # 👇 REQUIRED for Semgrep check
    if len(description) > 500:
        raise ValueError("Description too long.")
    
    return description

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        raise ValueError("Date must be YYYY-MM-DD.")
