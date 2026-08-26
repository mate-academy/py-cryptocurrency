from typing import Any
from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: Any) -> None:
    mock_prediction.return_value = 106

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: Any) -> None:
    mock_prediction.return_value = 94

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: Any) -> None:
    mock_prediction.return_value = 100

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_is_exactly_5_percent_higher(
    mock_prediction: Any,
) -> None:
    mock_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_is_exactly_5_percent_lower(
    mock_prediction: Any,
) -> None:
    mock_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"
