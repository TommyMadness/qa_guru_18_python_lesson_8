from dataclasses import dataclass
from enum import Enum


USER_ADULT_AGE = 18


class Status(Enum):
    student = "student"
    worker = "worker"


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE

    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items
    #
    # def __eq__(self, other):
    #     return (
    #         self.name == other.name
    #         and self.age == other.age
    #         and self.status == other.status
    #         and self.items == other.items
    #     )


class Worker(User):

    def __init__(self, name, age, items):
        self.name = name
        self.age = age
        self.items = items

    def do_work(self):
        pass


if __name__ == "__main__":
    d = {
        "name": "Oleg",
        "age": 16,
        "status": "student",
        "items": ["book", "pen", "paper"],
    }

    oleg = User(
        name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"]
    )
    oleg2 = User(
        name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"]
    )
    olga = User(name="Olga", age=18, status=Status.student, items=["book", "paper"])

    olga_worker = Worker(name="Olga", age=18, items=["book", "paper"])

    assert oleg == oleg2
    assert oleg.age == 16
    assert olga.age == 18
