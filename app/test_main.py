from __future__ import annotations
from unittest import mock
import pytest

from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @pytest.mark.parametrize(
        "current_rate,prediction_rate,expected",
        [
            pytest.param(
                10, 9.4, "Sell all your cryptocurrency",
                id="should sell below 0.95"
            ),
            pytest.param(
                10, 9.5, "Do nothing",
                id="should do nothing at boundary 0.95"
            ),
            pytest.param(
                10, 9.6, "Do nothing",
                id="should still do nothing at 0.96"
            ),
            pytest.param(
                10, 10.4, "Do nothing",
                id="should yet do nothing at 1.04"
            ),
            pytest.param(
                10, 10.5, "Do nothing",
                id="should do nothing at boundary 1.05"
            ),
            pytest.param(
                10, 10.6, "Buy more cryptocurrency",
                id="should just buy at 1.06"
            ),
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(
            self,
            mock_get_exchange_rate_prediction: mock.MagicMock,
            current_rate: float,
            prediction_rate: float,
            expected: str
    ) -> None:
        mock_get_exchange_rate_prediction.return_value = prediction_rate
        result = cryptocurrency_action(current_rate)
        assert result == expected
