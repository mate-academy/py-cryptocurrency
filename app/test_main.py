import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> float:
    with mock.patch("app.main.get_exchange_rate_prediction") as exchange_rate:
        yield exchange_rate


def test_buy_more_cryptocurrency(
        mocked_get_exchange_rate_prediction: float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.07
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_sell_all_your_cryptocurrency(
        mocked_get_exchange_rate_prediction: float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_do_nothing(
        mocked_get_exchange_rate_prediction: float
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
    mocked_get_exchange_rate_prediction.return_value = 1.01
    assert cryptocurrency_action(1) == "Do nothing"
