import streamlit as st

from backend import (
    init_tasks,
    get_tasks,
    mark_task_done,
    delete_task
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
# FILTRAGE DES TÂCHES (Nouveauté)
# =====================================

filtre = st.radio(
    "Filtrer les tâches :",
    options=["Toutes", "En cours", "Terminées"],
    horizontal=True
)

# =====================================
# AFFICHAGE DES TÂCHES
# =====================================

st.subheader("Liste des tâches")

# On passe le filtre sélectionné à la fonction backend
tasks_filtrees = get_tasks(filtre)

# on récupère l'index d'origine et la tâche
for original_index, task in tasks_filtrees:

    col1, col2, col3 = st.columns([0.8, 0.2, 0.2])

    with col1:
        status = (
            "Terminé"
            if task["done"]
            else "À faire"
        )

        st.write(
            f"{status} - {task['task']}"
        )

    with col2:
        if not task["done"]:
            # On utilise original_index pour que le bouton agisse sur la bonne tâche
            if st.button(
                "Marquer comme fait",
                key=f"done_{original_index}",
            ):
                mark_task_done(original_index)
                st.rerun()

    with col3:
        # On injecte le style CSS avec le bon original_index
        st.markdown(
            f"""
            <style>
            .st-key-delete_{original_index} button {{
                background-color: #d32f2f !important;
                color: white !important;
                border: 1px solid #b71c1c !important;
            }}

            .st-key-delete_{original_index} button:hover {{
                background-color: #b71c1c !important;
                color: white !important;
                border: 1px solid #8e0000 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # On utilise original_index pour la suppression
        if st.button(
            "Supprimer",
            key=f"delete_{original_index}"
        ):
            delete_task(original_index)
            st.rerun()