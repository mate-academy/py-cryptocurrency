from unittest import mock
import pytest
from app.main import cryptocurrency_action


class TestCryptoCurrency:
    @pytest.mark.parametrize(
        "prediction_rate,result",
        [
            (127, "Sell all your cryptocurrency"),
            (166, "Buy more cryptocurrency"),
            (152, "Do nothing"),
            (151.62, "Do nothing")
        ]
    )
    def test_main(self, prediction_rate: int | float, result: str):
        with mock.patch("app.main.get_exchange_rate_prediction") as rate:
            rate.return_value = prediction_rate
            assert cryptocurrency_action(144.4) == result
            rate.assert_called_once_with(144.4)
