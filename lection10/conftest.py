import datetime
import time

import pytest


@pytest.fixture(scope='class', autouse=True)
def start_stop_time():
    print(f'Start Time: {datetime.datetime.now()}')
    yield
    print(f'\nStop Time: {datetime.datetime.now()}\n')


@pytest.fixture()
def execution_time():
    start_time = time.perf_counter()
    yield
    print(f'\nRunTime: {round(time.perf_counter() - start_time, 3)}')