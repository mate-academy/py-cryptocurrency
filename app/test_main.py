import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_func() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction")\
            as mocked_function:
        yield mocked_function


def test_func_buy(mocked_func: callable) -> None:
    mocked_func.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_func_do_nothing(mocked_func: callable) -> None:
    mocked_func.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_func_sell(mocked_func: callable) -> None:
    mocked_func.return_value = 0.1
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
