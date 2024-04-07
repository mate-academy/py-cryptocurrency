import pytest
from unittest import mock
from typing import Any

from app.main import cryptocurrency_action


@pytest.fixture
def mocked_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_prediction):
        yield mocked_prediction


def test_cryptocurrency_action_should_return_buy(
        mocked_prediction: Any
) -> None:
    mocked_prediction.return_value = 5.2
    assert cryptocurrency_action(1.4) == "Buy more cryptocurrency", \
        "should return buy"


def test_cryptocurrency_action_should_return_sell(
        mocked_prediction: Any
) -> None:
    mocked_prediction.return_value = 0
    assert cryptocurrency_action(300) == "Sell all your cryptocurrency", \
        "should return sell"


def test_cryptocurrency_action_should_return_nothing(
        mocked_prediction: Any
) -> None:
    mocked_prediction.return_value = 20
    assert cryptocurrency_action(20) == "Do nothing", \
        "should return do nothing"


def test_cryptocurrency_action_for_first_limit(
        mocked_prediction: Any
) -> None:
    mocked_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing", \
        "should do nothing"


def test_cryptocurrency_action_for_second_limit(
        mocked_prediction: Any
) -> None:
    mocked_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing", \
        "should do nothing"
