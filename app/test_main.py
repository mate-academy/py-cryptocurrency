from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
class TestCryptoCurrencyPrediction:

    def test_should_buy_crypto(
            self, mocked_prediction: mock.MagicMock
    ) -> None:
        mocked_prediction.return_value = 1.1
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"

    def test_should_sell_crypto(
            self, mocked_prediction: mock.MagicMock
    ) -> None:
        mocked_prediction.return_value = 0.9
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

    def test_do_nothing_rate_95(
            self, mocked_prediction: mock.MagicMock
    ) -> None:
        mocked_prediction.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"

    def test_do_nothing_rate_105(
            self, mocked_prediction: mock.MagicMock
    ) -> None:
        mocked_prediction.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"
