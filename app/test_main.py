from unittest import mock
from typing import Any

import pytest

from app.main import cryptocurrency_action


@pytest.fixture()
def mocked_get_exchange_rate_prediction() -> Any:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        yield mocked_get_exchange_rate_prediction


@pytest.mark.parametrize("rate_prediction_value, expected_value", [
    pytest.param(1.5, "Buy more cryptocurrency",
                 id="test if prediction higher than current rate"),
    pytest.param(0.5, "Sell all your cryptocurrency",
                 id="test if prediction lower than current rate"),
    pytest.param(1, "Do nothing",
                 id="test if prediction equal current rate"),
    pytest.param(1.05, "Do nothing",
                 id="test should not buy cryptocurrency"),
    pytest.param(0.95, "Do nothing",
                 id="test should not buy cryptocurrency"),

])
def test_if_prediction_lower_than_current_rate(
        mocked_get_exchange_rate_prediction: Any,
        rate_prediction_value: float | int,
        expected_value: str,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = rate_prediction_value
    assert cryptocurrency_action(1) == expected_value
