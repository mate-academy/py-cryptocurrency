from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_for_buy(get_exchange_rate_prediction: MagicMock) -> None:

    get_exchange_rate_prediction.return_value = 105

    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_for_sell(get_exchange_rate_prediction: MagicMock) -> None:

    get_exchange_rate_prediction.return_value = 95

    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_for_do_nothing(get_exchange_rate_prediction: MagicMock) -> None:

    get_exchange_rate_prediction.return_value = 96

    result = cryptocurrency_action(100)
    assert result == "Do nothing"
