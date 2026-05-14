from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_buy_more(mock_prediction: MagicMock) -> None:
    current_rate = 100

    mock_prediction.return_value = 106

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_sell_all(mock_prediction: MagicMock) -> None:
    current_rate = 100

    mock_prediction.return_value = 94

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_do_nothing_upper_boundary(mock_prediction: MagicMock) -> None:
    current_rate = 100

    mock_prediction.return_value = 105

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_do_nothing_lower_boundary(mock_prediction: MagicMock) -> None:
    current_rate = 100

    mock_prediction.return_value = 95

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
