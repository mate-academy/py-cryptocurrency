from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value = 95)
def test_cryptocurrency_action_95(mock_get_exchange_rate_prediction: bool) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value = 105)
def test_cryptocurrency_action_105(mock_get_exchange_rate_prediction: bool) -> None:
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value = 106)
def test_cryptocurrency_action_104(mock_get_exchange_rate_prediction: bool) -> None:
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value = 94)
def test_cryptocurrency_action_96(mock_get_exchange_rate_prediction: bool) -> None:
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
