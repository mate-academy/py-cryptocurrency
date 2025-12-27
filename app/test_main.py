from __future__ import annotations

from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "input_current_rate,predicted_rate,expected_result",
        [
            pytest.param(100, 95, "Do nothing"),
            pytest.param(100, 105, "Do nothing"),
            pytest.param(100, 106, "Buy more cryptocurrency"),
            pytest.param(100, 94, "Sell all your cryptocurrency")
        ],
        ids=[
            "Should do nothing when difference not more than 5%",
            "Should do nothing when difference not more than 5%",
            "Should return sell when exchange rate dropped",
            "Should return buy when exchange rate increased"
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self,
                                   mock_prediction: MagicMock,
                                   input_current_rate: float | int,
                                   predicted_rate: float | int,
                                   expected_result: str) -> None:
        mock_prediction.return_value = predicted_rate
        assert cryptocurrency_action(input_current_rate) == expected_result
