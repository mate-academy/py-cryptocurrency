from unittest import mock, TestCase

from app.main import cryptocurrency_action


class TestCryptoCurrency(TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: float
    ) -> None:
        current = 50
        predicted = current * 1.06
        mock_get_exchange_rate_prediction.return_value = predicted

        result = cryptocurrency_action(current)
        self.assertEqual(result, "Buy more cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: float
    ) -> None:
        current = 50
        predicted = current * 0.94
        mock_get_exchange_rate_prediction.return_value = predicted

        result = cryptocurrency_action(current)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
            self,
            mock_get_exchange_rate_prediction: float
    ) -> None:
        current = 50
        predicted = current * 1.05
        mock_get_exchange_rate_prediction.return_value = predicted

        result = cryptocurrency_action(current)
        self.assertEqual(result, "Do nothing")

        current = 50
        predicted = current * 0.95
        mock_get_exchange_rate_prediction.return_value = predicted

        result = cryptocurrency_action(current)
        self.assertEqual(result, "Do nothing")
