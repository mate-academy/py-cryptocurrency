from typing import Union
import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: MagicMock,
        current_rate: Union[int, float],
        prediction_rate: float,
        expected: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected
