from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCruptocurrencyActions:

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: int
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 120

        assert (cryptocurrency_action(100) == "Buy more cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
            self,
            mock_get_exchange_rate_prediction: int
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = 80

        assert (cryptocurrency_action(100) == "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_105_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: int
    ) -> None:

        mock_get_exchange_rate_prediction.return_value = 105

        assert (cryptocurrency_action(100) == "Do nothing")

    @patch("app.main.get_exchange_rate_prediction")
    def test_rate_95_percent_do_nothing(
            self,
            mock_get_exchange_rate_prediction: int
    ) -> None:

        mock_get_exchange_rate_prediction.return_value = 95

        assert (cryptocurrency_action(100) == "Do nothing")
