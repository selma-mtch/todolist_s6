import streamlit as st

from backend import (
    init_tasks,
    get_tasks,
    mark_task_done,
    remove_task
)
from component.input import task_input_component

# =====================================
# INITIALISATION
# =====================================

init_tasks()

# =====================================
# INTERFACE
# =====================================

st.title("Ma TodoList")

# Ajout d'une tache
task_input_component()

# =====================================
# AFFICHAGE DES TÂCHES
# =====================================

st.subheader("Liste des tâches")

tasks = get_tasks()

for i, task in enumerate(tasks):

    col1, col2, col3 = st.columns([0.6, 0.2, 0.2])

    with col1:

        status = (
            "Terminé"
            if task["done"]
            else "À faire"
        )

        st.write(
            f"{status} - {task['task']} (échéance : {task['due_date']})"
        )

    with col2:

        if not task["done"]:

            if st.button(
                "Marquer comme fait",
                key=f"done_{i}"
            ):

                mark_task_done(i)
                st.rerun()

    with col3:

        if st.button("Supprimer", key=f"del_{i}"):

            remove_task(task["task"])
            st.rerun()