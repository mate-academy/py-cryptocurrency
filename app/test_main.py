import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_prediction() -> int:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_test_prediction):
        yield mocked_test_prediction


def test_function_return_buy_when_rate_is_high(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 12
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_function_return_sell_when_rate_is_low(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 6
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


def test_return_do_nothing_when_rate_is_equal(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"


def test_should_do_nothing_when_rate_1_05(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 10.5
    assert cryptocurrency_action(10) == "Do nothing"


def test_should_do_nothing_when_rate_0_95(mocked_prediction: int) -> None:
    mocked_prediction.return_value = 9.5
    assert cryptocurrency_action(10) == "Do nothing"
