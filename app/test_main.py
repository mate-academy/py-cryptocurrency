from typing import Union
from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize("prediction_rate, current_rate, expected",
                         [
                             pytest.param(
                                 1.1, 1, "Buy more cryptocurrency"),
                             pytest.param(
                                 0.9, 1, "Sell all your cryptocurrency"),
                             pytest.param(
                                 1.05, 1, "Do nothing"),
                             pytest.param(
                                 0.95, 1, "Do nothing")
                         ])
def test_buy_more_cryptocurrency(
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected
