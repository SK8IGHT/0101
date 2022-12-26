from src.database.models import Excavation as Model
from src.server.resolves.artifact import dbmanager


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        date_start=res[1],
        date_end=res[2],
        place_id=res[3],
        user_id=res[4]
    )


def get_all() -> list[Model] | dict:
    l = dbmanager.execute_query(
        query=f"select * from {Model.__name__}",
        fetchone=False)

    res = []

    if l:
        for res in l:
            res.append(Model(
                id=res[0],
                date_start=res[1],
                date_end=res[2],
                place_id=res[3],
                user_id=res[4]
            ))

    return res


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (date_start, date_end, placeID, userID) values(?,?,?,?) returning id",
        args=(new.date_start, new.date_end, new.place_id, new.user_id))

    if type(res) != dict:
        res = get(res[0])

    return ress


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (date_start, date_end, placeID, userID) = (?,?,?,?) where id=(?)",
        args=(new.date_start, new.date_end, new.place_id, new.user_id, id_))
