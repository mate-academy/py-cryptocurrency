from unittest.mock import patch
from typing import Any
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(mock_get_rate: Any) -> None:
    mock_get_rate.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(mock_get_rate: Any) -> None:
    mock_get_rate.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mock_get_rate: Any) -> None:
    mock_get_rate.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"

    mock_get_rate.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"

    mock_get_rate.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
