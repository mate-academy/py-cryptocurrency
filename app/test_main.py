from unittest import mock
from app.main import cryptocurrency_action


def test_forecast_higher_than_current_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=150):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_forecast_lower_than_current_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=90):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_forecast_at_the_lower_limit() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Do nothing"


def test_forecast_at_the_upper_limit() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Do nothing"


def test_forecast_in_the_middle() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=100):
        assert cryptocurrency_action(100) == "Do nothing"


def test_forecast_much_higher_than_current_rate() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=150):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_decimal_forecast_higher_than_current_rate() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=105.6
    ):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_decimal_forecast_lower_than_current_rate() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=94.5
    ):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
