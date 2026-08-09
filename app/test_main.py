from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: int) -> None:
    current_rate = 100
    mock_prediction.return_value = 106

    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: int) -> None:
    current_rate = 100
    mock_prediction.return_value = 94

    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: int) -> None:
    current_rate = 100
    mock_prediction.return_value = 102

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_noting_if_difference_bigger(mock_prediction: int) -> None:
    current_rate = 100
    mock_prediction.return_value = 105

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_noting_if_difference_less(mock_prediction: int) -> None:
    current_rate = 100
    mock_prediction.return_value = 95

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
