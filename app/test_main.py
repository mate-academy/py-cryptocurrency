from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_currency_action(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1
    assert cryptocurrency_action(
        1.0
    ) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_to_stay_if_close_to_buy_rate(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(
        1.0
    ) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_to_buy_if_close_to_buy_rate(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.93
    assert cryptocurrency_action(
        1.0
    ) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_to_sell_if_close_to_sell_rate(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.10
    assert cryptocurrency_action(
        1.0
    ) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_action_to_stay_if_close_to_sell_rate(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(
        1.0
    ) == "Do nothing"
