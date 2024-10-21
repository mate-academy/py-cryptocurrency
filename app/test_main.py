from unittest import mock
from app.main import cryptocurrency_action


def test_get_exchange_rate_prediction() -> None:
    current_rate = 100.0
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=106.0):
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=105.0):
        assert cryptocurrency_action(current_rate) == "Do nothing"
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=95.0):
        assert cryptocurrency_action(current_rate) == "Do nothing"
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=98.0):
        assert cryptocurrency_action(current_rate) == "Do nothing"
