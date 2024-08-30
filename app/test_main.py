from typing import Union
from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def get_exchange_rate_prediction() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as get_exchange_rate_prediction):
        yield get_exchange_rate_prediction


def test_should_return_sell_all_if_high(
        get_exchange_rate_prediction: Union[int, float]
) -> None:
    get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"


def test_should_return_do_nothing(
        get_exchange_rate_prediction: Union[int, float]
) -> None:
    get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"
