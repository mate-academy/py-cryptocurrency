from unittest import TestCase
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.05

        self.assertEqual(cryptocurrency_action(0.99999999999999
                                               ), "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.9499999999999999

        self.assertEqual(
            cryptocurrency_action(1.00000000001
                                  ), "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_if_1_05(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 1.05

        self.assertEqual(cryptocurrency_action(1
                                               ), "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_if_0_95(
            self,
            mock_get_exchange_rate_prediction: MagicMock
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 0.95

        self.assertEqual(cryptocurrency_action(1), "Do nothing")
