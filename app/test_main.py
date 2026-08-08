from unittest.mock import MagicMock
from app.main import cryptocurrency_action
from unittest import mock


@mock.patch("app.main.get_exchange_rate_prediction")
def test_if_we_should_buy_more(mock_get_exchange_rate: MagicMock) -> None:
    mock_get_exchange_rate.return_value = 2
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing(mock_get_exchange_rate: MagicMock) -> None:
    mock_get_exchange_rate.return_value = 19.95
    assert cryptocurrency_action(19.95) == "Do nothing"
    assert cryptocurrency_action(19) == "Do nothing"
    assert cryptocurrency_action(21) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all(mock_get_exchange_rate: MagicMock) -> None:
    mock_get_exchange_rate.return_value = 2
    assert cryptocurrency_action(5) == "Sell all your cryptocurrency"
