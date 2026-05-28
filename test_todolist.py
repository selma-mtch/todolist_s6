import datetime

from todolist_utils import add_task, remove_task, mark_task_done


# --- Tests unitaires (Partie 3) ---

def test_add_valid_task():
    tasks = []

    result = add_task(tasks, "Réviser le module", datetime.date.today())

    assert result is True
    assert len(tasks) == 1


def test_add_empty_task():
    tasks = []

    result = add_task(tasks, "", datetime.date.today())

    assert result is False
    assert len(tasks) == 0


def test_add_duplicate_task():
    tasks = [{
        "task": "Réviser le module",
        "done": False,
        "due_date": datetime.date.today(),
    }]

    result = add_task(tasks, "Réviser le module", datetime.date.today())

    assert result is False
    assert len(tasks) == 1


# --- Test d'intégration (Partie 4) : ajouter -> marquer fait -> supprimer ---

def test_task_lifecycle():
    tasks = []

    add_task(tasks, "Faire le TP", datetime.date.today())
    assert len(tasks) == 1

    mark_task_done(tasks, 0)
    assert tasks[0]["done"] is True

    remove_task(tasks, "Faire le TP")
    assert len(tasks) == 0


# --- Test de régression (Partie 5) : la règle anti-doublon ne doit jamais disparaître ---

def test_no_duplicate_regression():
    tasks = []

    add_task(tasks, "Projet maintenance", datetime.date.today())
    add_task(tasks, "Projet maintenance", datetime.date.today())

    assert len(tasks) == 1
