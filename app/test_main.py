from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
class TestCryptoAction:

    def test_should_buy_cryptocurrency(self, mocked_exchange_rate):
        mocked_exchange_rate.return_value = 1.1
        assert cryptocurrency_action(1) == "Buy more cryptocurrency!"

    def test_should_sell_cryptocurrency(self, mocked_exchange_rate):
        mocked_exchange_rate.return_value = 0.9
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency!"

    def test_should_output_do_nothing_if_105(self, mocked_exchange_rate):
        mocked_exchange_rate.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing!"

    def test_should_output_do_nothing_if_095(self, mocked_exchange_rate):
        mocked_exchange_rate.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing!"
