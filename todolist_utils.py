# Logique métier pure (sans Streamlit) — testable indépendamment.


def add_task(tasks, task, due_date):
    if task.strip() == "":
        return False

    if any(t["task"] == task for t in tasks):
        return False

    tasks.append({
        "task": task,
        "done": False,
        "due_date": due_date,
    })
    return True


def remove_task(tasks, task_name):
    for t in tasks:
        if t["task"] == task_name:
            tasks.remove(t)
            return True
    return False


def mark_task_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False
