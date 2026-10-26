from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.infrastructure.sql_repository import Base, SqlTodoRepository


def make_repo() -> SqlTodoRepository:
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    return SqlTodoRepository(sessionmaker(engine))


def test_add_and_get():
    repo = make_repo()
    todo = repo.add("write tests")
    assert todo.id == 1
    assert repo.get(todo.id).title == "write tests"
    assert repo.get(99) is None


def test_save_persists_changes():
    repo = make_repo()
    todo = repo.add("ship it")
    todo.complete()
    repo.save(todo)
    assert repo.get(todo.id).done is True


def test_list_ordered():
    repo = make_repo()
    repo.add("a")
    repo.add("b")
    assert [t.title for t in repo.list()] == ["a", "b"]
