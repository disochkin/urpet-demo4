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


# @app.get("/api/v1/orders")
# def get_orders(param=None):
#     global isUpdatedStatus
#     global message
#     buffer = ""
#     if isUpdatedStatus:
#         buffer = message
#         isUpdatedStatus = False
#         message = ""
#     if param:
#         return {"repo": [order for order in repo if order.id == int(param)], "message": buffer}
#     return {"repo": repo, "message": buffer}
#

# @app.post("/api/v1/orders")
# def create_order(data=Body()):
#     repo.append(Order(
#         data["id"],
#         data["start_date"],
#         data["device"],
#         data["problem_type"],
#         data["problem_description"],
#         data["client"],
#         data["status"]))
#     return
#
#
# @app.post("/api/v1/update")
# def update_order(dto: Annotated[UpdateOrderDto, Form()]):
#     global isUpdatedStatus
#     global message
#     for order in repo:
#         if order.id == dto.id:
#             if (dto.status != "") and (order.status != dto.status):
#                 order.status = dto.status
#                 isUpdatedStatus = True
#                 message += "Статус  заяки № " + str(order.id) + " изменен\n"
#                 if dto.status == "выполнено":
#                     message += "Заяка № " + str(order.id) + " выполнена\n"
#                     order.end_date = datetime.now()
#             if dto.problem_description != "":
#                 order.problem_description = dto.problem_description
#             if dto.master != "":
#                 order.master = dto.master
#             if dto.comment:
#                 order.comments += dto.comment + "\n"
#             return order
#     return "Нет такого"
#
#
# def complete_count():
#     return len([order for order in repo if order.status == "выполнено"])
#
#
# def get_problem_type_stat():
#     stat = defaultdict(int)
#     for order in repo:
#         if order.status == "выполнено":
#             stat[order.problem_type] += 1
#     return stat
#
#
# def avg_time():
#     times = [(order.end_date - order.start_date).days for order in repo
#              if order.status == "выполнено"]
#     return sum(times) / complete_count()
#
#
# @app.get("/api/v1/get_stat")
# def get_stat():
#     return {
#         "complete_count": complete_count(),
#         "problem_type_stat": get_problem_type_stat(),
#         "avg_time": avg_time()}
