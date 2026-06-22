# fichier : backend.py

import streamlit as st

# Initialisation des tâches
def init_tasks():
    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []

# Ajouter une tâche
def add_task(task_name):
    if task_name.strip() != "":
        st.session_state["tasks"].append({
            "task": task_name,
            "done": False
        })

# Récupérer les tâches
def get_tasks(filter_status="Toutes"):
    tasks_with_index = list(enumerate(st.session_state["tasks"]))
    
    if filter_status == "En cours":
        return [(idx, task) for idx, task in tasks_with_index if not task["done"]]
    elif filter_status == "Terminées":
        return [(idx, task) for idx, task in tasks_with_index if task["done"]]
    
    # Par défaut : "Toutes"
    return tasks_with_index

# Marquer une tâche comme faite
def mark_task_done(index):
    st.session_state["tasks"][index]["done"] = True

# Supprimer une tâche
def delete_task(index):
    del st.session_state["tasks"][index]