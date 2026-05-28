import logging
import streamlit as st
from backend import init_tasks, add_task, mark_task_done, get_tasks

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")


def setup_function():
    st.session_state.clear()


def test_mark_task_done():
    logging.info("Start Test mark_task_done")

    init_tasks()
    add_task("Réviser")

    mark_task_done(0)

    tasks = get_tasks()

    assert tasks[0]["done"] is True

    logging.info(f"[OK] {tasks}")