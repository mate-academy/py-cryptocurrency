from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: int) -> None:
    mock_prediction.return_value = 106

    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_now(mock_prediction: int) -> None:
    mock_prediction.return_value = 94

    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_nothing_to_do1(mock_prediction: int) -> None:
    mock_prediction.return_value = 95

    result = cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_nothing_to_do2(mock_prediction: int) -> None:
    mock_prediction.return_value = 105

    result = cryptocurrency_action(100)

    assert result == "Do nothing"
