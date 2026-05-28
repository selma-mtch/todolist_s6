# fichier : backend.py — adaptateur Streamlit (session_state + logs)
# La logique métier vit dans todolist_utils.py pour être testable sans Streamlit.

import logging

import streamlit as st

import todolist_utils

logging.basicConfig(level=logging.INFO)


# Initialisation des tâches
def init_tasks():

    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []


# Ajouter une tâche
def add_task(task_name, due_date):

    success = todolist_utils.add_task(
        st.session_state["tasks"], task_name, due_date
    )

    if success:
        logging.info("Ajout d'une tâche : %s", task_name)
    else:
        logging.warning("Ajout refusé (tâche vide ou doublon) : %r", task_name)

    return success


# Récupérer les tâches
def get_tasks():

    return st.session_state["tasks"]


# Supprimer une tâche
def remove_task(task_name):

    success = todolist_utils.remove_task(st.session_state["tasks"], task_name)

    if success:
        logging.info("Suppression d'une tâche : %s", task_name)

    return success


# Marquer une tâche comme faite
def mark_task_done(index):

    return todolist_utils.mark_task_done(st.session_state["tasks"], index)
