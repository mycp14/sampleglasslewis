from app.domain.entities import Todo, TodoNotFoundError
from app.domain.repositories import TodoRepository


class CreateTodo:
    def __init__(self, repo: TodoRepository) -> None:
        self._repo = repo

    def execute(self, title: str) -> Todo:
        return self._repo.add(title)


class ListTodos:
    def __init__(self, repo: TodoRepository) -> None:
        self._repo = repo

    def execute(self) -> list[Todo]:
        return self._repo.list()


class CompleteTodo:
    def __init__(self, repo: TodoRepository) -> None:
        self._repo = repo

    def execute(self, todo_id: int) -> Todo:
        todo = self._repo.get(todo_id)
        if todo is None:
            raise TodoNotFoundError(todo_id)
        todo.complete()
        self._repo.save(todo)
        return todo
