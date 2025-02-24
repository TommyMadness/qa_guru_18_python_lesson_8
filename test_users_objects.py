import csv

import pytest

from models.providers import (
    UserProvider,
    CsvUserProvider,
    DatabaseuserProvider,
    ApiUserProvider,
)
from models.users import User, USER_ADULT_AGE, Status, Worker


@pytest.fixture(params=[CsvUserProvider, DatabaseuserProvider, ApiUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()


@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture
def workers(users) -> list[Worker]:

    workers = [
        Worker(name=user.name, age=user.age, items=user.items)
        for user in users
        if user.status == Status.worker
    ]
    return workers


def test_workers_are_adults_v3(workers):

    for worker in workers:
        assert worker.is_adult(), f"Worker {worker.name} младше {USER_ADULT_AGE} лет"
