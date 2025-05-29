import uuid
from datetime import datetime
from logging import NullHandler
from uuid import UUID

from sqlmodel import Field, SQLModel


class Task(SQLModel, table=True):
    uuid:UUID | None = Field(default=None, primary_key=True)
    register_datetime: datetime
    start_datetime: datetime | None = None
    end_datetime: datetime | None = None
    device: str
    problem_type: str
    problem_description: str
    client: str
    master: str | None = None
    status: str
    comments: str

    def __init__(self, device, problem_type, problem_description, client, comments):
        self.uuid = uuid.uuid4()
        self.register_datetime = datetime.now()
        self.start_datetime = None
        self.end_datetime = None
        self.device = device
        self.problem_type = problem_type
        self.problem_description = problem_description
        self.client = client
        self.master = None
        self.status = "в ожидании"
        self.comments = comments


    def start_task(self, master):
        if self.status == "в ожидании":
            self.start_datetime = datetime.now()
            self.status = "в работе"
            self.master = master
        else:
            raise f'Задачу в состоянии {self.status} нельзя взять в работу.'

    def  end_task(self, comments):
        if self.status == "в работе":
            self.end_date = datetime.now()
            self.comments = comments
        else:
            raise f'Задачу в состоянии {self.status} нельзя завершить.'

    # @uuid.setter
    # def uuid(self, value):
    #     self._uuid = value
