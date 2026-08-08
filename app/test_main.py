from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action_with_various_conditions() -> None:
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=106):
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=94):
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=100):
        assert cryptocurrency_action(100) == "Do nothing"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=105):
        assert cryptocurrency_action(100) == "Do nothing"
    with mock.patch("app.main.get_exchange_rate_prediction", return_value=95):
        assert cryptocurrency_action(100) == "Do nothing"
