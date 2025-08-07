from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    def test_buy_more_cryptocurrency_when_prediction_5_percent_higher(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 106
            result = cryptocurrency_action(100)
            assert result == "Buy more cryptocurrency"
            mock_prediction.assert_called_once_with(100)

    def test_buy_more_cryptocurrency_when_prediction_much_higher(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 150
            result = cryptocurrency_action(100)
            assert result == "Buy more cryptocurrency"

    def test_sell_all_cryptocurrency_when_prediction_5_percent_lower(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 94
            result = cryptocurrency_action(100)
            assert result == "Sell all your cryptocurrency"
            mock_prediction.assert_called_once_with(100)

    def test_sell_all_cryptocurrency_when_prediction_much_lower(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 50
            result = cryptocurrency_action(100)
            assert result == "Sell all your cryptocurrency"

    def test_do_nothing_when_prediction_within_5_percent_higher(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 104
            result = cryptocurrency_action(100)
            assert result == "Do nothing"

    def test_do_nothing_when_prediction_within_5_percent_lower(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 96
            result = cryptocurrency_action(100)
            assert result == "Do nothing"

    def test_do_nothing_when_prediction_exactly_same(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 100
            result = cryptocurrency_action(100)
            assert result == "Do nothing"

    def test_boundary_case_exactly_5_percent_higher(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 105
            result = cryptocurrency_action(100)
            assert result == "Do nothing"

    def test_boundary_case_exactly_5_percent_lower(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 95
            result = cryptocurrency_action(100)
            assert result == "Do nothing"

    def test_with_float_values(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 106.0
            result = cryptocurrency_action(100.5)
            assert result == "Buy more cryptocurrency"
            mock_prediction.assert_called_once_with(100.5)

    def test_with_small_values(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 0.94
            result = cryptocurrency_action(1)
            assert result == "Sell all your cryptocurrency"

    def test_with_large_values(
            self
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
            mock_prediction.return_value = 10400
            result = cryptocurrency_action(10000)
            assert result == "Do nothing"
