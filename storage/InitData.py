from models.TaskModel import CreateTaskModel
from storage.Repository import TaskRepository


def init_data(user_repo : TaskRepository):

    user_repo.createTask(CreateTaskModel(
        device="printer",
        problem_type="error",
        problem_description="problem1",
        client="Иванов",
        comments="comment1"))

    user_repo.createTask(CreateTaskModel(
        device="monitor",
        problem_type="not work",
        problem_description="smoke",
        client="Иванов",
        comments="comment2"))

    user_repo.createTask(CreateTaskModel(
        device="printer",
        problem_type="low toner",
        problem_description="black",
        client="Иванов",
        comments="comment3"))