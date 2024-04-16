from unittest import mock

import pytest
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction, expected", [
        pytest.param(100, 110, "Buy more cryptocurrency"),
        pytest.param(100, 90, "Sell all your cryptocurrency"),
        pytest.param(100, 100, "Do nothing"),
        pytest.param(100, 105, "Do nothing"),
        pytest.param(100, 95, "Do nothing"),
    ])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_main(mocked_exchange_rate_prediction: None,
              prediction: Union[int, float],
              current_rate: Union[int, float],
              expected: str
              ) -> None:
    mocked_exchange_rate_prediction.return_value = prediction
    result = cryptocurrency_action(current_rate)
    assert result == expected
