import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_erp:
        yield mocked_erp


def test_buy_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.08
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.8
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_95_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


def test_105_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: callable) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
