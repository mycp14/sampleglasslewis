from dataclasses import dataclass


class TodoNotFoundError(Exception):
    def __init__(self, todo_id: int) -> None:
        super().__init__(f"Todo {todo_id} not found")
        self.todo_id = todo_id


@dataclass
class Todo:
    id: int
    title: str
    done: bool = False

    def complete(self) -> None:
        self.done = True
