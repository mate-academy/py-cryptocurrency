from unittest import mock
import pytest
from app.main import cryptocurrency_action


class TestCryptoCurrency:
    @pytest.mark.parametrize(
        "prediction_rate,result",
        [
            (80, "Sell all your cryptocurrency"),
            (155, "Buy more cryptocurrency"),
            (95, "Do nothing"),
            (105, "Do nothing")
        ]
    )
    def test_main(self, prediction_rate: int | float, result: str) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction") as rate:
            rate.return_value = prediction_rate
            assert cryptocurrency_action(100) == result
            rate.assert_called_once_with(100)
