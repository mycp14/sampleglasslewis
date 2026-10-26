from functools import lru_cache

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.application.use_cases import CompleteTodo, CreateTodo, ListTodos
from app import config
from app.domain.repositories import TodoRepository
from app.infrastructure.in_memory_repository import InMemoryTodoRepository
from app.infrastructure.sql_repository import Base, SqlTodoRepository


@lru_cache
def get_repository() -> TodoRepository:
    if config.DATABASE_URL:
        engine = create_engine(config.DATABASE_URL, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        return SqlTodoRepository(sessionmaker(engine))
    return InMemoryTodoRepository()


def get_create_todo(repo: TodoRepository = Depends(get_repository)) -> CreateTodo:
    return CreateTodo(repo)


def get_list_todos(repo: TodoRepository = Depends(get_repository)) -> ListTodos:
    return ListTodos(repo)


def get_complete_todo(repo: TodoRepository = Depends(get_repository)) -> CompleteTodo:
    return CompleteTodo(repo)
