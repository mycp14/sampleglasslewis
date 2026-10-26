from abc import ABC, abstractmethod

from app.domain.entities import Todo


class TodoRepository(ABC):
    @abstractmethod
    def add(self, title: str) -> Todo: ...

    @abstractmethod
    def get(self, todo_id: int) -> Todo | None: ...

    @abstractmethod
    def list(self) -> list[Todo]: ...

    @abstractmethod
    def save(self, todo: Todo) -> None: ...
