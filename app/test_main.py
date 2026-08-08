import pytest
from unittest import mock
from app.main import cryptocurrency_action
from typing import Union


@pytest.mark.parametrize(
    "prediction_rate, expected",
    [
        (1.06, "Buy more cryptocurrency"),
        (0.94, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1, "Do nothing"),
        (1.05, "Do nothing"),
    ],
)
class TestClass():
    def test_cryptocurrency_action(self,
                                   prediction_rate: Union[int, float],
                                   expected: str) -> None:
        current_rate = 1
        with (mock.patch("app.main.get_exchange_rate_prediction")
              as get_rate_prediction):
            get_rate_prediction.return_value = prediction_rate

            result = cryptocurrency_action(current_rate)

            get_rate_prediction.assert_called_once_with(current_rate)

            assert result == expected
