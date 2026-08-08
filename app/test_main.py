import pytest

from unittest import mock

from typing import Any

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        yield mocked_get_exchange_rate_prediction


def test_cryptocurrency_calls_function(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 20
    cryptocurrency_action(20)
    mocked_get_exchange_rate_prediction.assert_called_once_with(20)


def test_cryptocurrency_return_buy(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.6
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_return_sell(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_return_do_nothing(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_boundary_condition_top(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_boundary_condition_bottom(
        mocked_get_exchange_rate_prediction: Any
) -> None:
    mocked_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
