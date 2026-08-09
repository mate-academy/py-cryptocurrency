from unittest import mock

from app.main import cryptocurrency_action


def test_get_exchange_rate_prediction() -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = 2
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"

        mock_prediction.return_value = 5
        assert cryptocurrency_action(6) == "Sell all your cryptocurrency"

        mock_prediction.return_value = 105
        assert cryptocurrency_action(100) == "Do nothing"

        mock_prediction.return_value = 95
        assert cryptocurrency_action(100) == "Do nothing"

        mock_prediction.return_value = 1
        assert cryptocurrency_action(1) == "Do nothing"
