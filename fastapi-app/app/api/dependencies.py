from functools import lru_cache

from fastapi import Depends

from app.application.use_cases import CompleteTodo, CreateTodo, ListTodos
from app.domain.repositories import TodoRepository
from app.infrastructure.in_memory_repository import InMemoryTodoRepository


@lru_cache
def get_repository() -> TodoRepository:
    return InMemoryTodoRepository()


def get_create_todo(repo: TodoRepository = Depends(get_repository)) -> CreateTodo:
    return CreateTodo(repo)


def get_list_todos(repo: TodoRepository = Depends(get_repository)) -> ListTodos:
    return ListTodos(repo)


def get_complete_todo(repo: TodoRepository = Depends(get_repository)) -> CompleteTodo:
    return CompleteTodo(repo)
