from unittest import mock
from unittest.mock import MagicMock

import pytest

from typing import Union

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "exchange_rate, current_rate, expected",
        [
            (0, 10100, "Sell all your cryptocurrency"),
            (4.8798, 5.2576, "Sell all your cryptocurrency"),
            (95, 100, "Do nothing"),
            (102.0, 107.3, "Do nothing"),
            (31.5, 30, "Do nothing"),
            (12, 10, "Buy more cryptocurrency"),
            (0.45, 0.36, "Buy more cryptocurrency"),
        ],
        ids=[
            "Function calculates exchange rate as 0",
            "Prediction rate less 0.95",
            "Prediction rate equal to 0.95",
            "Prediction rate more 0.95 and less 1.05",
            "Prediction rate equal to 1.05",
            "Prediction rate more 1.05",
            "Prediction rate more 1.05, two numbers after dot",
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_exchange_rate: MagicMock,
            exchange_rate: Union[int, float],
            current_rate: Union[int, float],
            expected: str
    ) -> None:
        mock_exchange_rate.return_value = exchange_rate

        assert cryptocurrency_action(current_rate) == expected
