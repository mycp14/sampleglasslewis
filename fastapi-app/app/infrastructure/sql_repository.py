from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from app.domain.entities import Todo
from app.domain.repositories import TodoRepository


class Base(DeclarativeBase):
    pass


class TodoModel(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    done: Mapped[bool] = mapped_column(default=False)

    def to_entity(self) -> Todo:
        return Todo(id=self.id, title=self.title, done=self.done)


class SqlTodoRepository(TodoRepository):
    def __init__(self, session_factory: sessionmaker) -> None:
        self._session_factory = session_factory

    def add(self, title: str) -> Todo:
        with self._session_factory.begin() as session:
            model = TodoModel(title=title)
            session.add(model)
            session.flush()
            return model.to_entity()

    def get(self, todo_id: int) -> Todo | None:
        with self._session_factory() as session:
            model = session.get(TodoModel, todo_id)
            return model.to_entity() if model else None

    def list(self) -> list[Todo]:
        with self._session_factory() as session:
            models = session.query(TodoModel).order_by(TodoModel.id).all()
            return [m.to_entity() for m in models]

    def save(self, todo: Todo) -> None:
        with self._session_factory.begin() as session:
            model = session.get(TodoModel, todo.id)
            if model:
                model.title = todo.title
                model.done = todo.done
