from typing import Union

import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action, get_exchange_rate_prediction


class TestCryptocurrencyAction:

    @pytest.mark.parametrize(
        "current_rate, predicted_rate, expected",
        [
            # Buy more scenarios (predicted > 5% higher than current)
            (100, 105.01, "Buy more cryptocurrency"),  # 5.01% increase
            (50, 52.51, "Buy more cryptocurrency"),  # 5.02% increase
            (200, 210.01, "Buy more cryptocurrency"),  # 5.005% increase
            (1000, 1050.01, "Buy more cryptocurrency"),  # 5.001% increase
            (1, 1.0501, "Buy more cryptocurrency"),  # 5.01% increase

            # Sell all scenarios (predicted > 5% lower than current)
            (100, 94.99, "Sell all your cryptocurrency"),  # 5.01% decrease
            (50, 47.49, "Sell all your cryptocurrency"),  # 5.02% decrease
            (200, 189.99, "Sell all your cryptocurrency"),  # 5.005% decrease
            (1000, 949.99, "Sell all your cryptocurrency"),  # 5.001% decrease
            (1, 0.9499, "Sell all your cryptocurrency"),  # 5.01% decrease

            # Do nothing scenarios (within ±5%)
            (100, 105, "Do nothing"),  # Exactly 5% increase - boundary
            (100, 95, "Do nothing"),  # Exactly 5% decrease - boundary
            (100, 104.99, "Do nothing"),  # 4.99% increase
            (100, 95.01, "Do nothing"),  # 4.99% decrease
            (100, 100, "Do nothing"),  # No change
            (100, 102, "Do nothing"),  # 2% increase
            (100, 98, "Do nothing"),  # 2% decrease
            (100, 104.9999, "Do nothing"),  # Just below 5% increase
            (100, 95.0001, "Do nothing"),  # Just below 5% decrease
        ]
    )
    def test_cryptocurrency_action_various_scenarios(
            self,
            current_rate: Union[int, float],
            predicted_rate: float,
            expected: str
    ) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_predict:
            mock_predict.return_value = predicted_rate
            result: str = cryptocurrency_action(current_rate)

            assert result == expected
            mock_predict.assert_called_once_with(current_rate)

    def test_cryptocurrency_action_with_integer_rate(self) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_predict:
            mock_predict.return_value = 110.5
            result: str = cryptocurrency_action(100)

            assert result == "Buy more cryptocurrency"

    def test_cryptocurrency_action_with_float_rate(self) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_predict:
            mock_predict.return_value = 94.5
            result: str = cryptocurrency_action(100.0)

            assert result == "Sell all your cryptocurrency"

    def test_edge_case_zero_current_rate(self) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_predict:
            mock_predict.return_value = 0.0001
            result: str = cryptocurrency_action(0.001)

            assert result == "Sell all your cryptocurrency"

    def test_precision_handling(self) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_predict:
            mock_predict.return_value = 100 * 1.050001
            result: str = cryptocurrency_action(100)

            assert result == "Buy more cryptocurrency"

    def test_get_exchange_rate_prediction_not_mocked(self) -> None:
        result: float = get_exchange_rate_prediction(100)
        assert isinstance(result, float)

    def test_multiple_calls(self) -> None:
        with patch("app.main.get_exchange_rate_prediction") as mock_predict:
            mock_predict.side_effect = [110, 90, 103]

            result1: str = cryptocurrency_action(100)
            result2: str = cryptocurrency_action(100)
            result3: str = cryptocurrency_action(100)

            assert result1 == "Buy more cryptocurrency"
            assert result2 == "Sell all your cryptocurrency"
            assert result3 == "Do nothing"

            assert mock_predict.call_count == 3
