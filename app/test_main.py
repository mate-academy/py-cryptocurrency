from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(
        self,
        mock_exchange_rate_prediction: int | float
    ) -> None:
        mock_exchange_rate_prediction.return_value = 1.06
        assert cryptocurrency_action(1) == "Buy more cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(
        self,
        mock_exchange_rate_prediction: int | float
    ) -> None:
        mock_exchange_rate_prediction.return_value = 0.94
        assert cryptocurrency_action(1) == "Sell all your cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(
        self,
        mock_exchange_rate_prediction: int | float
    ) -> None:
        mock_exchange_rate_prediction.return_value = 1.02
        assert cryptocurrency_action(1) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_edge_case_increase(
        self,
        mock_exchange_rate_prediction: int | float
    ) -> None:
        mock_exchange_rate_prediction.return_value = 1.05
        assert cryptocurrency_action(1) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_edge_case_decrease(
        self,
        mock_exchange_rate_prediction: int | float
    ) -> None:
        mock_exchange_rate_prediction.return_value = 0.95
        assert cryptocurrency_action(1) == "Do nothing"
