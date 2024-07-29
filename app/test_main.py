import pytest
from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:

    @pytest.mark.parametrize(
        "current_rate, predicted_rate, expected_result",
        [
            (100, 107, "Buy more cryptocurrency"),
            (100, 93, "Sell all your cryptocurrency"),
            (100, 101, "Do nothing"),
            (100, 98, "Do nothing"),
            (100, 105, "Do nothing"),
            (100, 95, "Do nothing"),
        ]
    )
    def test_cryptocurrency_action(self,
                                   current_rate: int | float,
                                   predicted_rate: float,
                                   expected_result: str) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction",
                        return_value=predicted_rate):
            result = cryptocurrency_action(current_rate)
            assert result == expected_result
