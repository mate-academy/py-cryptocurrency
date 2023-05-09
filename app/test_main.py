from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_when_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: MagicMock) -> None:

    mock_get_exchange_rate_prediction.return_value = 106.0

    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_when_sell_cryptocurrency(
        mock_get_exchange_rate_prediction: MagicMock) -> None:

    mock_get_exchange_rate_prediction.return_value = 94.0

    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_when_do_nothing(
        mock_get_exchange_rate_prediction: MagicMock) -> None:

    mock_get_exchange_rate_prediction.return_value = 95.0
    assert cryptocurrency_action(100.0) == "Do nothing"
    mock_get_exchange_rate_prediction.return_value = 105.0
    assert cryptocurrency_action(100.0) == "Do nothing"
