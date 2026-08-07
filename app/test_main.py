from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


class TestCryptoCurrency:
    @pytest.mark.parametrize(
        "current_rate,prediction_rate,action",
        [
            pytest.param(
                10,
                15,
                "Buy more cryptocurrency",
                id="should buy cryptocurrency`",
            ),
            pytest.param(
                10,
                5,
                "Sell all your cryptocurrency",
                id="should sell cryptocurrency",
            ),
            pytest.param(
                10,
                9.5,
                "Do nothing",
                id="should return `Do nothing`",
            ),
            pytest.param(
                1,
                1.05,
                "Do nothing",
                id="should not buy any cryptocurrency",
            ),
        ],
    )
    def test_cryptocurrency_action(
            self,
            current_rate: float | int,
            prediction_rate: int | float,
            action: str,
    ) -> None:
        with patch(
                "app.main.get_exchange_rate_prediction",
                return_value=prediction_rate
        ) as mock_get_exchange_rate_prediction:
            result = cryptocurrency_action(current_rate)
            mock_get_exchange_rate_prediction.assert_called_once_with(
                current_rate
            )
            assert result == action
