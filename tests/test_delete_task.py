import logging
import streamlit as st
from backend import init_tasks, add_task, delete_task, get_tasks

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")


def setup_function():
    st.session_state.clear()


def test_delete_task():
    logging.info("delete_task")

    init_tasks()

    add_task("Tâche 1")
    add_task("Tâche 2")

    delete_task(0)

    tasks = get_tasks()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Tâche 2"

    logging.info(f" {tasks}")