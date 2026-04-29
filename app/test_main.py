from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_105(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_095(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
