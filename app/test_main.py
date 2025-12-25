import pytest
from unittest import mock
from typing import Union
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @pytest.mark.parametrize(
        "current_rate, predicted_rate, expected_result",
        [
            (100, 106, "Buy more cryptocurrency"),
            (100, 94, "Sell all your cryptocurrency"),
            (100, 104, "Do nothing"),
            (100, 96, "Do nothing"),
            (100, 105, "Do nothing"),
            (100, 95, "Do nothing"),
        ]
    )
    def test_cryptocurrency_action(self,
                                   current_rate: Union[int, float],
                                   predicted_rate: float,
                                   expected_result: str) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction",
                        return_value=predicted_rate):
            result = cryptocurrency_action(current_rate)
            assert result == expected_result
