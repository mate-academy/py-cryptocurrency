from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(get_exchange_rate_prediction: MagicMock)\
        -> None:
    get_exchange_rate_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"
    get_exchange_rate_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_upper(get_exchange_rate_prediction: MagicMock) -> None:
    get_exchange_rate_prediction.return_value = 80
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
    get_exchange_rate_prediction.assert_called_once()


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_lower(get_exchange_rate_prediction: MagicMock) -> None:
    get_exchange_rate_prediction.return_value = 103
    assert cryptocurrency_action(100) == "Do nothing"
    get_exchange_rate_prediction.assert_called_once()
