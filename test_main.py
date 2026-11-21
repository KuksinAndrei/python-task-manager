from src.main import tasks, add_task, list_tasks, complete_task


def setup_function():
    tasks.clear()


def test_add_task():
    add_task("Тест")
    assert len(list_tasks()) == 1


def test_complete_task():
    add_task("Тест")
    complete_task(0)
    assert list_tasks()[0]["done"] is True