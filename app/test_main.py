import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action



@patch("app.main.get_exchange_rate_prediction", return_value=102)
def test_cryptocurrency_action_of_expected_do_nothing(prediction_rate) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"
    prediction_rate.assert_called_once_with(current_rate)

@patch("app.main.get_exchange_rate_prediction", return_value=98)
def test_cryptocurrency_action_of_expected_do_nothing(prediction_rate) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Do nothing"
    prediction_rate.assert_called_once_with(current_rate)

@patch("app.main.get_exchange_rate_prediction", return_value=105.1)
def test_cryptocurrency_action_of_expected_do_nothing(prediction_rate) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
    prediction_rate.assert_called_once_with(current_rate)

@patch("app.main.get_exchange_rate_prediction", return_value=94.9)
def test_cryptocurrency_action_of_expected_do_nothing(prediction_rate) -> None:
    current_rate = 100
    assert cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"
    prediction_rate.assert_called_once_with(current_rate)


# "Buy more cryptocurrency", если прогнозируемый обменный курс более чем на 5% выше текущего.
# "Sell all your cryptocurrency", если прогнозируемый обменный курс более чем на 5% ниже текущего.
# "Do nothing", если разница не так уж велика.