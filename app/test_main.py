from unittest.mock import patch

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    def test_exchange_rate_will_raise(self) -> None:
        with (patch(
            "app.main.get_exchange_rate_prediction",
            return_value=1.05
        )):
            result = cryptocurrency_action(1)
            assert result == "Buy more cryptocurrency"

    def test_exchange_rate_will_fall(self) -> None:
        with (patch(
            "app.main.get_exchange_rate_prediction",
            return_value=0.95
        )):
            result = cryptocurrency_action(1)
            assert result == "Sell all your cryptocurrency"

    def test_exchange_rate_will_not_change(self) -> None:
        with (patch(
            "app.main.get_exchange_rate_prediction",
            return_value=1
        )):
            result = cryptocurrency_action(1)
            assert result == "Do nothing"


