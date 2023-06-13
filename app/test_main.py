from app.main import cryptocurrency_action
from unittest import mock
import pytest


@pytest.fixture
def mocked_exchange_rate_prediction() -> None:
    with mock.patch("main.get_exchange_rate_prediction") as mocked_function:
        yield mocked_function


def test_cryptocurrency_action_buy_more(
        mocked_exchange_rate_prediction: None
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.07
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(
        mocked_exchange_rate_prediction: None
) -> None:
    mocked_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
        mocked_exchange_rate_prediction: None
) -> None:
    mocked_exchange_rate_prediction.return_value = 1.0
    assert cryptocurrency_action(1.0) == "Do nothing"
