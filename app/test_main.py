from unittest.mock import patch

from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    with patch("app.main.get_exchange_rate_prediction") as prediction_rate:
        prediction_rate.return_value = 1.06
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"

        prediction_rate.return_value = 0.94
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

        prediction_rate.return_value = 1.01
        assert cryptocurrency_action(1) == "Do nothing"

        prediction_rate.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"

        prediction_rate.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"
