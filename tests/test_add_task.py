import logging
import streamlit as st
from backend import init_tasks, add_task, get_tasks

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")


def setup_function():
    st.session_state.clear()


def test_add_task():
    logging.info("add_task")

    init_tasks()
    add_task("Acheter du pain")

    tasks = get_tasks()

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Acheter du pain"
    assert tasks[0]["done"] is False

    logging.info(f"tasks = {tasks}")
