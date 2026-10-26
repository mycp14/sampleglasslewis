from pydantic import BaseModel, Field


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class TodoResponse(BaseModel):
    id: int
    title: str
    done: bool
