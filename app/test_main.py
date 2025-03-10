from unittest.mock import patch
from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    current_rate = 100.0

    with patch("app.main.get_exchange_rate_prediction", return_value=106.0):
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"

    with (patch("app.main.get_exchange_rate_prediction", return_value=94.0)):
        assert (cryptocurrency_action(current_rate)
                == "Sell all your cryptocurrency")

    with patch("app.main.get_exchange_rate_prediction", return_value=105.0):
        assert cryptocurrency_action(current_rate) == "Do nothing"

    with patch("app.main.get_exchange_rate_prediction", return_value=95.0):
        assert cryptocurrency_action(current_rate) == "Do nothing"
