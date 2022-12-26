from src.database.models import Artifact as Model
from src.database.dbmanager import DbManager
import settings

dbmanager = DbManager(db_path=settings.DATABASE_PATH)


def get(id_: int) -> Model | None:
    res = dbmanager.execute_query(
        query=f'select * from {Model.__name__} where id=(?)',
        args=(id_,))

    return None if not res else Model(
        id=res[0],
        name=res[1],
        age=res[2],
        culture_id=res[3]
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
                name=res[1],
                age=res[2],
                culture_id=res[3]
            ))

    return res


def delete(id_: int) -> None:
    return dbmanager.execute_query(
        query=f'delete from {Model.__name__} where id=(?)',
        args=(id_,))


def create(new: Model) -> int | dict:
    res = dbmanager.execute_query(
        query=f"insert into {Model.__name__} (name, age, cultureID) values(?) returning id",
        args=(new.name, new.age, new.culture_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(id_: int, new: Model) -> None:
    return dbmanager.execute_query(
        query=f"update {Model.__name__} set (name, age, cultureId) = (?) where id=(?)",
        args=(new.name, new.age, new.culture_id, id_))
