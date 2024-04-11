import pytest


@pytest.fixture(scope='module')
def set_up():
    print('Начало теста!')
    yield
    print('Конец теста!')
