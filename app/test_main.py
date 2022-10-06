import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_exchange_rate() -> mock.Mock:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_exchange):
        yield mocked_exchange


def test_buy_more(mocked_exchange_rate: mock.Mock) -> None:
    mocked_exchange_rate.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_everything(mocked_exchange_rate: mock.Mock) -> None:
    mocked_exchange_rate.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing(mocked_exchange_rate: mock.Mock) -> None:
    mocked_exchange_rate.return_value = 1.01
    assert cryptocurrency_action(1) == "Do nothing"
