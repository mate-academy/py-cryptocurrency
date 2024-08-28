from unittest import mock
from app.main import cryptocurrency_action


def test_cryptocurrency_action() -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=1.06
    ):
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=0.94
    ):
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=0.95
    ):
        assert cryptocurrency_action(1) == "Do nothing"
    with mock.patch(
            "app.main.get_exchange_rate_prediction", return_value=1.05
    ):
        assert cryptocurrency_action(1) == "Do nothing"