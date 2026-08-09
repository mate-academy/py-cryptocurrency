from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.10)
def test_buy_more_cryptocurrency(mock_cryptocurrency: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.90)
def test_sell_all_your_cryptocurrency(mock_cryptocurrency: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_max_value_do_nothing(mock_cryptocurrency: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_min_value_do_nothing(mock_cryptocurrency: MagicMock) -> None:
    result = cryptocurrency_action(1.0)
    assert result == "Do nothing"
