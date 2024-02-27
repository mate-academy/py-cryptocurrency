import unittest
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_buy_more(
            self,
            mocked_get_exchange_rate_prediction: mock.Mock
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 1.06
        assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_sell_all(
            self,
            mocked_get_exchange_rate_prediction: mock.Mock
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 0.91
        assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_do_nothing_with_rate_0_95(
            self,
            mocked_get_exchange_rate_prediction: mock.Mock
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 0.95
        assert cryptocurrency_action(1.0) == "Do nothing"

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action_do_nothing_with_rate_1_05(
            self,
            mocked_get_exchange_rate_prediction: mock.Mock
    ) -> None:
        mocked_get_exchange_rate_prediction.return_value = 1.05
        assert cryptocurrency_action(1.0) == "Do nothing"
