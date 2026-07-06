from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_buy(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_sell(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 101
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing_high_limit(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing_lower_limit(mock_rate_prediction: MagicMock) -> None:
    mock_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"