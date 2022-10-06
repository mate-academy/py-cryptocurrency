import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange() -> mock.Mock:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_exchange):
        yield mocked_exchange


def test_buy_more(mocked_get_exchange: mock.Mock) -> None:
    mocked_get_exchange.return_value = 1.37
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all(mocked_get_exchange: mock.Mock) -> None:
    mocked_get_exchange.return_value = 0.87
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing_not_much_less(mocked_get_exchange: mock.Mock) -> None:
    mocked_get_exchange.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_not_much_more(mocked_get_exchange: mock.Mock) -> None:
    mocked_get_exchange.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
