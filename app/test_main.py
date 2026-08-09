from unittest import mock
from app.main import cryptocurrency_action


def test_crypto_action_prediction() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
            as mock_rate_prediction):
        mock_rate_prediction.return_value = 110.0
        result = cryptocurrency_action(100)
        assert result == "Buy more cryptocurrency"

    with (mock.patch("app.main.get_exchange_rate_prediction")
            as mock_rate_prediction):
        mock_rate_prediction.return_value = 90.0
        result = cryptocurrency_action(100)
        assert result == "Sell all your cryptocurrency"

    with (mock.patch("app.main.get_exchange_rate_prediction")
            as mock_rate_prediction):
        mock_rate_prediction.return_value = 95.0
        result = cryptocurrency_action(100)
        assert result == "Do nothing"

    with (mock.patch("app.main.get_exchange_rate_prediction")
            as mock_rate_prediction):
        mock_rate_prediction.return_value = 105.0
        result = cryptocurrency_action(100)
        assert result == "Do nothing"
