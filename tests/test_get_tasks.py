import logging
import streamlit as st
from backend import init_tasks, add_task, get_tasks

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")


def setup_function():
    st.session_state.clear()


def test_get_tasks():
    logging.info("[TEST] get_tasks")

    init_tasks()
    add_task("Faire les courses")

    tasks = get_tasks()

    assert isinstance(tasks, list)
    assert len(tasks) == 1
    assert tasks[0][1]["task"] == "Faire les courses"
    assert tasks[0][1]["done"] is False

    logging.info(f"[OK] {tasks}")