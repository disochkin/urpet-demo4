from sqlmodel import col, or_
from sqlmodel.sql.expression import SelectOfScalar
from models.Task import Task


def status_filter(
        buffer_query: SelectOfScalar[Task],
        value: str | None) -> SelectOfScalar[Task]:
    if value == None:
        return buffer_query

    if value.lower() not in ["в ожидании", "в работе", "выполнено"]:
        raise Exception("Некорректный статус")
    return buffer_query.where(User.gender == value)  # type: ignore


def search(
        buffer_query: SelectOfScalar[Task],
        value: str | None) -> SelectOfScalar[Task]:
    if value is None:
        return buffer_query
    return buffer_query.where(or_(col(Task.problem_description).contains(value.lower()),
                                  col(Task.problem_type).contains(value.lower()),
                                  col(Task.master).contains(value.lower())))


def pagination(
        buffer_query: SelectOfScalar[Task],
        size: int | None,
        num: int | None) -> SelectOfScalar[Task]:
    if size is None or num is None:
        return buffer_query

    return buffer_query.offset(size * num).limit(size)


def sort(buffer_list: SelectOfScalar[Task],
         field: str | None = None,
         sort_type: int | None = None) -> SelectOfScalar[Task]:
    if (field is None or sort_type is None):
        return buffer_list

    if (field == "name" and sort_type == 0):
        return buffer_list.order_by(User.name)
    if (field == "name" and sort_type == 1):
        return buffer_list.order_by(User.name.desc())
    if (field == "age" and sort_type == 0):
        return buffer_list.order_by(User.age)
    if (field == "age" and sort_type == 1):
        return buffer_list.order_by(User.age.desc())
    raise Exception("Неожиданная ошибка в сортировке")
