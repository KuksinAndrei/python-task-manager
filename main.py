"""Консольный менеджер задач."""

tasks = []


def add_task(title):
    """Добавляет задачу в список."""
    tasks.append({"title": title, "done": False})


def list_tasks():
    """Возвращает список всех задач."""
    return tasks


def complete_task(index):
    """Отмечает задачу выполненной."""
    tasks[index]["done"] = True


def main():
    add_task("Выучить Git")
    add_task("Сделать лабораторную")
    complete_task(0)
    for i, task in enumerate(list_tasks(), 1):
        status = "x" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")


if __name__ == "__main__":
    main()