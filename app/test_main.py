import pytest
from unittest.mock import patch
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_action",
    [
        pytest.param(35.5,
                     17.8,
                     "Buy more cryptocurrency",
                     id="Test buy crypto"),
        pytest.param(17.8,
                     35.5,
                     "Sell all your cryptocurrency",
                     id="Test sell crypto"),
        pytest.param(35.5,
                     35.6,
                     "Do nothing",
                     id="Test do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: callable,
        prediction_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_action: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_action
