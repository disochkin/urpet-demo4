from datetime import datetime
from uuid import UUID
from sqlalchemy import Engine
from sqlmodel import SQLModel, Session, create_engine, select
from models.Task import Task
from storage.TaskDataActions import status_filter, pagination, search, sort
from models.TaskModel import CreateTaskModel, UpdateTaskModel, ReadTaskModel
import os.path

from models.TaskModel import CreateTaskModel


class TaskRepositoryDB:
    __path: str
    __engine: Engine

    def __init__(self):
        self.__path = "database.db"
        self.__engine = create_engine(f"sqlite:///{self.__path}")

        if not os.path.exists(self.__path):
            SQLModel.metadata.create_all(self.__engine)
            init_data(self)

    def __add(self, create_model: CreateTaskModel) -> None:
        task: Task = Task(create_model.device,
                          create_model.problem_type,
                          create_model.problem_description,
                          create_model.comments,
                          create_model.client)
        with Session(self.__engine) as session:
            session.add(task)
            session.commit()

    def createTask(self, create_model: CreateTaskModel) -> None:
        self.__add(create_model)

    def read(self,
             search_value: str | None,
             filter_value: str | None,
             sort_field: str | None,
             sort_type: int | None,
             page_size: int | None,
             page_num: int | None) -> list[ReadTaskModel]:

        with Session(self.__engine) as session:
            b0 = select(Task)
            b1 = search(b0, search_value)
            b2 = status_filter(b1, filter_value)
            b3 = sort(b2, sort_field, sort_type)
            b4 = pagination(b3, page_size, page_num)
            tasks = session.exec(b4).all()
        result = [ReadTaskModel(
            uuid=task.uuid,
            register_datetime=task.register_datetime,
            start_datetime=task.start_datetime,
            end_datetime=task.end_datetime,
            device=task.device,
            problem_type=task.problem_type,
            problem_description=task.problem_description,
            client=task.client,
            master=task.master,
            status=task.status,
            comments=task.comments)
            for task in tasks]
        return result


    def read_by_id(self, uuid: UUID) -> ReadTaskModel | None:
        with Session(self.__engine) as session:
            statement = select(Task).where(Task.uuid == uuid)
            task = session.exec(statement).first()

        if task == None:
            raise Exception("Задача не найдена")

        return ReadTaskModel(
            uuid=task.uuid,
            register_datetime=task.register_datetime,
            start_datetime=task.start_datetime,
            end_datetime=task.end_datetime,
            device=task.device,
            problem_type=task.problem_type,
            problem_description=task.problem_description,
            client=task.client,
            master=task.master,
            status=task.status,
            comments=task.comments)




def init_data(task_repo: TaskRepositoryDB):
    # region init_data
    task_repo.createTask(CreateTaskModel(
        device="printer",
        problem_type="error",
        problem_description="problem1",
        client="Иванов",
        comments="comment1"))

    task_repo.createTask(CreateTaskModel(
        device="monitor",
        problem_type="not work",
        problem_description="smoke",
        client="Иванов",
        comments="comment2"))

    task_repo.createTask(CreateTaskModel(
        device="printer",
        problem_type="low toner",
        problem_description="black",
        client="Иванов",
        comments="comment3"))    # endregion`
