from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CreateTaskModel(BaseModel):
    device: str
    problem_type: str
    problem_description: str
    client: str
    comments: str


class ReadTaskModel(BaseModel):
    uuid: UUID
    register_datetime: datetime | None
    start_datetime: datetime | None
    end_datetime: datetime | None
    device: str | None
    problem_type: str | None
    problem_description: str | None
    client: str | None
    master: str | None
    status: str | None
    comments: str | None


class UpdateTaskModel(BaseModel):
    start_datetime: datetime | None
    end_datetime: datetime | None
    status: str | None
    problem_description: Optional[str] = ""
    master: Optional[str] = ""
    comments: Optional[str] = ""
