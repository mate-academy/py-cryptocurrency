from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_cryptocurrency(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 111
    result = cryptocurrency_action(current_rate=100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_your_cryptocurrency(
        mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 79
    result = cryptocurrency_action(current_rate=100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(current_rate=100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(current_rate=100)
    assert result == "Do nothing"
