from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_cripto(mock_get_exchange: mock.MagicMock) -> None:
    mock_get_exchange.return_value = 11.23
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_cripto(mock_get_exchange: mock.MagicMock) -> None:
    mock_get_exchange.return_value = 8.21
    assert cryptocurrency_action(11.23) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_white(mock_get_exchange: mock.MagicMock) -> None:
    mock_get_exchange.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
    mock_get_exchange.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
