from collections import defaultdict
from datetime import datetime
from typing import Optional, Annotated

import uvicorn
from fastapi import FastAPI, Form, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
repo = []


class Order:
    def __init__(self, id, start_date, device, problem_type, problem_description, client, status):
        self.id = id
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = None
        self.device = device
        self.problem_type = problem_type
        self.problem_description = problem_description
        self.client = client
        self.master = "не назначено"
        self.status = "в ожидании"
        self.comments = ""


class UpdateOrderDto(BaseModel):
    id: int
    status: Optional[str] = ""
    problem_description: Optional[str] = ""
    master: Optional[str] = ""
    comment: Optional[str] = ""


order1 = Order(1, "2024-03-10", "printer", "error", "", "Иванов", "")
order2 = Order(2, "2024-04-10", "monitor", "not work", "smoke", "Иванов", "")
order3 = Order(3, "2024-05-10", "printer", "low toner", "black", "Иванов", "")
repo.append(order1)
repo.append(order2)
repo.append(order3)
isUpdatedStatus = False
message = ""


@app.get("/api/v1/orders")
def get_orders(param=None):
    global isUpdatedStatus
    global message
    buffer = ""
    if isUpdatedStatus:
        buffer = message
        isUpdatedStatus = False
        message = ""
    if param:
        return {"repo": [order for order in repo if order.id == int(param)], "message": buffer}
    return {"repo": repo, "message": buffer}


@app.post("/api/v1/orders")
def create_order(data=Body()):
    repo.append(Order(
        data["id"],
        data["start_date"],
        data["device"],
        data["problem_type"],
        data["problem_description"],
        data["client"],
        data["status"]))
    return


@app.post("/api/v1/update")
def update_order(dto: Annotated[UpdateOrderDto, Form()]):
    global isUpdatedStatus
    global message
    for order in repo:
        if order.id == dto.id:
            if (dto.status != "") and (order.status != dto.status):
                order.status = dto.status
                isUpdatedStatus = True
                message += "Статус  заяки № " + str(order.id) + " изменен\n"
                if dto.status == "выполнено":
                    message += "Заяка № " + str(order.id) + " выполнена\n"
                    order.end_date = datetime.now()
            if dto.problem_description != "":
                order.problem_description = dto.problem_description
            if dto.master != "":
                order.master = dto.master
            if dto.comment:
                order.comments += dto.comment + "\n"
            return order
    return "Нет такого"


def complete_count():
    return len([order for order in repo if order.status == "выполнено"])


def get_problem_type_stat():
    stat = defaultdict(int)
    for order in repo:
        if order.status == "выполнено":
            stat[order.problem_type] += 1
    return stat


def avg_time():
    times = [(order.end_date - order.start_date).days for order in repo
             if order.status == "выполнено"]
    return sum(times) / complete_count()


@app.get("/api/v1/get_stat")
def get_stat():
    return {
        "complete_count": complete_count(),
        "problem_type_stat": get_problem_type_stat(),
        "avg_time": avg_time()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
