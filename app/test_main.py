from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency_edge_case(self,
                                               mock_get_prediction: Mock
                                               ) -> None:
        current_rate = 100.0
        mock_get_prediction.return_value = 100.0 * 1.050000000000001
        result = cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency_edge_case(self,
                                               mock_get_prediction: Mock
                                               ) -> None:
        current_rate = 100.0
        mock_get_prediction.return_value = 100.0 * 0.9499999999999999
        result = cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_at_exact_upper_boundary(self,
                                                mock_get_prediction: Mock
                                                ) -> None:
        current_rate = 100.0
        mock_get_prediction.return_value = 100.0 * 1.05
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_at_exact_lower_boundary(self,
                                                mock_get_prediction: Mock
                                                ) -> None:
        current_rate = 100.0
        mock_get_prediction.return_value = 100.0 * 0.95
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"
