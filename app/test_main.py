from typing import Union
from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize("prediction_rate, current_rate, expected",
                         [
                             (1.07, 1, "Buy more cryptocurrency"),
                             (0.93, 1, "Sell all your cryptocurrency"),
                             (1.04, 1, "Do nothing"),
                             (0.94, 1, "Do nothing"),
                         ])
def test_buy_more_cryptocurrency(
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected
