# app/test_main.py
import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "current_rate, prediction_rate, expected",
        [
            pytest.param(
                100, 106, "Buy more cryptocurrency",
                id="above_5_percent_buy",
            ),
            pytest.param(
                100, 105, "Do nothing",
                id="exactly_5_percent_up_boundary_no_buy",
            ),
            pytest.param(
                100, 100, "Do nothing",
                id="no_change",
            ),
            pytest.param(
                100, 95, "Do nothing",
                id="exactly_5_percent_down_boundary_no_sell",
            ),
            pytest.param(
                100, 94, "Sell all your cryptocurrency",
                id="below_5_percent_sell",
            ),
        ],
    )
    def test_cryptocurrency_action(
        self, current_rate: int, prediction_rate: int, expected: str
    ) -> None:
        with patch(
            "app.main.get_exchange_rate_prediction",
            return_value=prediction_rate,
        ):
            assert cryptocurrency_action(current_rate) == expected
