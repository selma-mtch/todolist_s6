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
def get_tasks():

    return st.session_state["tasks"]

# Marquer une tâche comme faite
def mark_task_done(index):

    st.session_state["tasks"][index]["done"] = True


# Supprimer une tâche
def delete_task(index):

    del st.session_state["tasks"][index]