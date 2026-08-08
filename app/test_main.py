from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_1(get_exchange_rate_prediction: MagicMock) -> None:
    get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_2(get_exchange_rate_prediction: MagicMock) -> None:
    get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_3(get_exchange_rate_prediction: MagicMock) -> None:
    get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_4(get_exchange_rate_prediction: MagicMock) -> None:
    get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"
