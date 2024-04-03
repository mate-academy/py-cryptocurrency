from unittest import TestCase, mock, main

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy(
            self, get_exchange_rate_prediction: mock.MagicMock
    ) -> None:
        get_exchange_rate_prediction.return_value = 1.06
        self.assertEqual(cryptocurrency_action(1), "Buy more cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_sell(
            self, get_exchange_rate_prediction: mock.MagicMock
    ) -> None:
        get_exchange_rate_prediction.return_value = 0.9
        self.assertEqual(
            cryptocurrency_action(1),
            "Sell all your cryptocurrency"
        )

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self, get_exchange_rate_prediction: mock.MagicMock
    ) -> None:
        get_exchange_rate_prediction.return_value = 1.05
        self.assertEqual(cryptocurrency_action(1), "Do nothing")


if __name__ == "__main__":
    main()
