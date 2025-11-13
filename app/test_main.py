from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyBasic():

    def test_cryptocurrency_action_can_return_buy_more(
            self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction") as mock_exchange:
            mock_exchange.return_value = 25
            assert cryptocurrency_action(15) == "Buy more cryptocurrency"

    def test_cryptocurrency_action_can_return_sell(
            self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction") as mock_exchange:
            mock_exchange.return_value = 10
            assert cryptocurrency_action(15) == "Sell all your cryptocurrency"

    def test_cryptocurrency_action_can_return_nothing(
            self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction") as mock_exchange:
            mock_exchange.return_value = 15
            assert cryptocurrency_action(15) == "Do nothing"


class TestCryptocurrencyEdgeCases():

    def test_cryptocurrency_action_return_do_nothing_with_105_percent(
            self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction") as mock_exchange:
            mock_exchange.return_value = 21
            assert cryptocurrency_action(20) == "Do nothing"

    def test_cryptocurrency_action_return_do_nothing_with_95_percent(
            self) -> None:
        with mock.patch(
                "app.main.get_exchange_rate_prediction") as mock_exchange:
            mock_exchange.return_value = 19
            assert cryptocurrency_action(20) == "Do nothing"
