import pytest


@pytest.fixture(scope='module')
def set_up():
    """fixture разграничения тестов в терминале"""
    print('Начало теста!')
    yield
    print('Конец теста!')
