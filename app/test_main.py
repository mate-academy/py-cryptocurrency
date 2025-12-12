from .main import cryptocurrency_action
from unittest import mock
from unittest.mock import MagicMock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: MagicMock) -> None:
    current = 100
    mock_prediction.return_value = 106  # +6%
    assert cryptocurrency_action(current) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: MagicMock) -> None:
    current = 100
    mock_prediction.return_value = 90  # -10%
    assert cryptocurrency_action(current) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: MagicMock) -> None:
    current = 100
    mock_prediction.return_value = 103  # +3%
    assert cryptocurrency_action(current) == "Do nothing"
