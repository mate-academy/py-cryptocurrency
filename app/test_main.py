from app.main import cryptocurrency_action
from unittest.mock import patch, Mock


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_by_more(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_105(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing_95(mock_prediction: Mock) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
