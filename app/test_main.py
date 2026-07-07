from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Any


@patch("app.main.get_exchange_rate_prediction")
def test_for_cryptocurrency_action_when_increase_more_than_5_percent(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_for_cryptocurrency_action_when_increase_exactly_5_percent(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_for_cryptocurrency_action_when_decrease_more_then_5_percent(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_for_cryptocurrency_action_when_decrease_exactly_5_percent(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_for_cryptocurrency_action_when_no_change(
        mock_prediction: Any
) -> None:
    mock_prediction.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
