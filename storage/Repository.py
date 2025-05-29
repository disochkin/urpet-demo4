from uuid import UUID

from models.Task import Task
from models.TaskModel import CreateTaskModel, ReadTaskModel, UpdateTaskModel


class TaskRepository:
    __tasks = []

    def createTask(self, create_model: CreateTaskModel) -> UUID:
        uuid = self.__add(create_model)
        return uuid

    def __add(self, create_model: CreateTaskModel) -> UUID:
        task: Task = Task(device=create_model.device,
                          problem_type=create_model.problem_type,
                          problem_description=create_model.problem_description,
                          client=create_model.client,
                          comments=create_model.comments)
        self.__tasks.append(task)
        return task.uuid

    def read_by_id(self, uuid: UUID) -> ReadTaskModel | None:
        for task in self.__tasks:
            if (task.uuid == uuid):
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
        raise Exception(f"Таска с uuid={self.uuid} не найден")

    def read_all_tasks(self):
        fetched_data = []
        for task in self.__tasks:
            fetched_data.append(ReadTaskModel(
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
                comments=task.comments))
        return fetched_data

    def update_task(self, uuid: UUID, updatedTask: UpdateTaskModel):
        for task in self.__tasks:
            if task.uuid == uuid:
                if updatedTask.start_datetime is not None:
                    task.start_datetime = updatedTask.start_datetime
                if updatedTask.end_date is not None:
                    task.end_datetime = updatedTask.end_datetime
                if updatedTask.master is not None:
                    task.master = updatedTask.master
                if updatedTask.problem_description is not None:
                    task.problem_description = updatedTask.problem_description
                if updatedTask.status is not None:
                    task.status = updatedTask.status
                if updatedTask.comments is not None:
                    task.comments = updatedTask.comments

    def delete(self, uuid: UUID) -> None:
        for task in self.__tasks:
            if (task.uuid == uuid):
                self.__tasks.remove(task)
                return None
        raise Exception("Задача не найдена")
