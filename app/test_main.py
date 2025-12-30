from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Callable


@patch("app.main.get_exchange_rate_prediction", return_value=102)
def test_cryptocurrency_action_of_expected_correct_result_1(
    prediction_rate: Callable
) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"
    prediction_rate.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction", return_value=98)
def test_cryptocurrency_action_of_expected_correct_result_2(
    prediction_rate: Callable
) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"
    prediction_rate.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction", return_value=105.1)
def test_cryptocurrency_action_of_expected_correct_result_3(
    prediction_rate: Callable
) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
    prediction_rate.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction", return_value=94.9)
def test_cryptocurrency_action_of_expected_correct_result_4(
    prediction_rate: Callable
) -> None:
    current_rate = 100
    assert (
        cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"
    )
    prediction_rate.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_cryptocurrency_action_of_expected_correct_result_5(
    prediction_rate: Callable
) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"
    prediction_rate.assert_called_once_with(current_rate)


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_cryptocurrency_action_of_expected_correct_result_6(
    prediction_rate: Callable
) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"
    prediction_rate.assert_called_once_with(current_rate)
