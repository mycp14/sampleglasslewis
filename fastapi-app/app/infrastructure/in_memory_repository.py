from app.domain.entities import Todo
from app.domain.repositories import TodoRepository


class InMemoryTodoRepository(TodoRepository):
    def __init__(self) -> None:
        self._items: dict[int, Todo] = {}
        self._next_id = 1

    def add(self, title: str) -> Todo:
        todo = Todo(id=self._next_id, title=title)
        self._items[todo.id] = todo
        self._next_id += 1
        return todo

    def get(self, todo_id: int) -> Todo | None:
        return self._items.get(todo_id)

    def list(self) -> list[Todo]:
        return list(self._items.values())

    def save(self, todo: Todo) -> None:
        self._items[todo.id] = todo
