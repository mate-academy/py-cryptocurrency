from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.fixture()
def mocked_prediction() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        yield mocked_prediction


def test_buy_cryptocurrency(mocked_prediction: None) -> None:
    mocked_prediction.return_value = 5
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_sell_cryptocurrency(mocked_prediction: None) -> None:
    mocked_prediction.return_value = 1
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_buy_nothing(mocked_prediction: None) -> None:
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_sell_nothing(mocked_prediction: None) -> None:
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
