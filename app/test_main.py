from unittest import mock, TestCase
from typing import Callable
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy_cryptocurrency(self, mock_exchange_rate: Callable) -> None:
        mock_exchange_rate.return_result(210)
        assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_sell_cryptocurrency(self, mock_exchange_rate: Callable) -> None:
        mock_exchange_rate.return_result(90)
        assert cryptocurrency_action(100) == "Sell all your cryptocurrency"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self, mock_exchange_rate: Callable) -> None:
        mock_exchange_rate.return_result(100.0)
        assert cryptocurrency_action(100.0) == "Do nothing"
