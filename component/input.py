import datetime

import streamlit as st

from backend import add_task


# saisie d'une tâche avec la touche Entrée et le bouton Ajouter
def task_input_component():
    def _process_add():
        task = st.session_state.get("custom_task_input", "")
        due_date = st.session_state.get("custom_due_date", datetime.date.today())

        if add_task(task, due_date):
            st.session_state["custom_task_input"] = ""  # Vide le champ
            st.session_state["add_warning"] = ""
        else:
            st.session_state["add_warning"] = (
                "Impossible d'ajouter la tâche (vide ou déjà existante)."
            )

    st.text_input(
        "Ajouter une tâche",
        key="custom_task_input",
        on_change=_process_add,
    )

    st.date_input(
        "Date d'échéance",
        key="custom_due_date",
    )

    st.button("Ajouter", on_click=_process_add)

    if st.session_state.get("add_warning"):
        st.warning(st.session_state["add_warning"])
