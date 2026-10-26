from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_complete_todo, get_create_todo, get_list_todos
from app.api.schemas import TodoCreate, TodoResponse
from app.application.use_cases import CompleteTodo, CreateTodo, ListTodos
from app.domain.entities import TodoNotFoundError

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(body: TodoCreate, use_case: CreateTodo = Depends(get_create_todo)):
    return use_case.execute(body.title)


@router.get("", response_model=list[TodoResponse])
def list_todos(use_case: ListTodos = Depends(get_list_todos)):
    return use_case.execute()


@router.post("/{todo_id}/complete", response_model=TodoResponse)
def complete_todo(todo_id: int, use_case: CompleteTodo = Depends(get_complete_todo)):
    try:
        return use_case.execute(todo_id)
    except TodoNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
