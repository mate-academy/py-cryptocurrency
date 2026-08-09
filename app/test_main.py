import pytest

from typing import Union
from unittest import mock

from app.main import cryptocurrency_action


class TestCryptocurrency:
    @pytest.mark.parametrize(
        "current_rate, prediction_rate, expected_action",
        [
            (100, 106.0, "Buy more cryptocurrency"),
            (100.0, 94.0, "Sell all your cryptocurrency"),
            (100, 102, "Do nothing"),
            (100.0, 98, "Do nothing"),
            (200, 190, "Do nothing"),
            (200, 210, "Do nothing"),
        ],
        ids=[
            "Buy more cryptocurrency",
            "Sell all your cryptocurrency",
            "Do nothing",
            "Do nothing",
            "Do nothing when prediction_rate / current_rate == 0.95",
            "Do nothing when prediction_rate / current_rate == 1.05"
        ]
    )
    @mock.patch("app.main.get_exchange_rate_prediction")
    def test_cryptocurrency_action(self,
                                   mocked_prediction_rate: mock.Mock,
                                   current_rate: Union[int, float],
                                   prediction_rate: Union[int, float],
                                   expected_action: str) -> None:
        mocked_prediction_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == expected_action
        mocked_prediction_rate.assert_called_once_with(current_rate)
