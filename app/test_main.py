from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCryptocurrency:
    @pytest.mark.parametrize(
        "prediction,result",
        [
            (512, "Buy more cryptocurrency"),
            (128, "Sell all your cryptocurrency"),
            (243.2, "Do nothing"),
            (268.8, "Do nothing"),
        ],
    )
    def test_main(self, prediction: int | float, result: str) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction") as predict:
            predict.return_value = prediction
            assert cryptocurrency_action(256) == result
            predict.assert_called_once_with(256)
