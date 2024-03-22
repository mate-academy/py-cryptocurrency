from typing import Union
from unittest import mock
import pytest
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @mock.patch("app.main.get_exchange_rate_prediction")
    @pytest.mark.parametrize(
        "current_rate,prediction_rate,expected_result",
        [
            (1, 0.95, "Do nothing"),
            (1, 1.05, "Do nothing"),
            (1, 1.06, "Buy more cryptocurrency",),
            (1, 0.9, "Sell all your cryptocurrency"),
        ]
    )
    def test_cryptocurrency_action(self,
                                   mocked_prediction: mock,
                                   current_rate: Union[int, float],
                                   prediction_rate: Union[int, float],
                                   expected_result: str) -> None:
        mocked_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_result
