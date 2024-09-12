from unittest import mock

from app.main import cryptocurrency_action

from typing import Callable


def test_should_return_str() -> None:
    assert isinstance(cryptocurrency_action(3), str)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_is_called(
        mocked_get_prediction: Callable
) -> None:
    mocked_get_prediction.return_value = 2.2
    cryptocurrency_action(2)


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_buy_if_value_2(mocked_get_prediction: Callable) -> None:
    mocked_get_prediction.return_value = 2.2

    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_rate_1_05(
        mocked_get_prediction: Callable
) -> None:
    mocked_get_prediction.return_value = 2.1

    assert cryptocurrency_action(2) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_do_nothing_if_rate_0_95(
        mocked_get_prediction: Callable
) -> None:
    mocked_get_prediction.return_value = 1.9

    assert cryptocurrency_action(2) == "Do nothing"
