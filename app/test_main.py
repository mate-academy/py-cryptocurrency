from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_buy(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 106
    expected = "Buy more cryptocurrency"
    result = cryptocurrency_action(100)

    assert result == expected


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_sell(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 94
    expected = "Sell all your cryptocurrency"
    result = cryptocurrency_action(100)

    assert result == expected


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_do_nothing(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 105
    expected = "Do nothing"
    result = cryptocurrency_action(100)

    assert result == expected


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_do_nothing_upper_lim(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 95
    expected = "Do nothing"
    result = cryptocurrency_action(100)

    assert result == expected
