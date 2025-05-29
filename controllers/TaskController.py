from uuid import UUID
from fastapi_controllers import Controller
from fastapi_controllers.routing import delete, get, post, put
from storage.InitData import init_data
from models.TaskModel import CreateTaskModel, UpdateTaskModel
from storage.TaskRepositoryDB import TaskRepositoryDB

class TaskController(Controller):
    task_repo = TaskRepositoryDB()

    @get("/tasks/{uuid}")
    def get_task_by_id(self, uuid: UUID):
        try:
            return self.task_repo.read_by_id(uuid)
        except Exception as e:
            return str(e)

    @get("/tasks")
    def get_tasks(self):
        try:
            return self.task_repo.read(
                search_value=None,
                filter_value=None,
                sort_field=None,
                sort_type=None,
                page_size=None,
                page_num=None)
        except Exception as e:
            return str(e)

    @post("/create/task")
    def create_order(self, create_task: CreateTaskModel):
        uuid = self.task_repo.createTask(create_task)
        return f"Задача c {uuid} успешно создана"

    @put("/update/task/{uuid}")
    def update_task(self, uuid : UUID, update_task : UpdateTaskModel):
        try:
            self.task_repo.update_task(uuid, update_task)
            return f"Задача c {uuid} успешно обновлена"
        except Exception as e:
            return e

    @delete("/tasks/{uuid}")
    def delete_user(self, uuid : UUID):
        try:
            self.task_repo.delete(uuid)
            return "Задача успешно удалена"
        except Exception as e:
            return str(e)

