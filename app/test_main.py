from unittest import mock

import pytest

from app.main import cryptocurrency_action


class TestCryptocurrency:
    @pytest.mark.parametrize(
        "prediction,result",
        [
            (200, "Buy more cryptocurrency"),
            (50, "Sell all your cryptocurrency"),
            (95, "Do nothing"),
            (105, "Do nothing"),
        ],
    )
    def test_main(self, prediction: int | float, result: str) -> None:
        with mock.patch("app.main.get_exchange_rate_prediction") as predict:
            predict.return_value = prediction
            assert cryptocurrency_action(100) == result
            predict.assert_called_once_with(100)
