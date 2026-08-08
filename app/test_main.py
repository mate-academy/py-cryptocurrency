import pytest
from unittest import mock
from app.main import cryptocurrency_action
from unittest.mock import MagicMock
from typing import Union


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 250, "Buy more cryptocurrency"),
        (100, 30, "Sell all your cryptocurrency"),
        (100, 102, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    current_rate: Union[int, float],
    prediction_rate: Union[int, float],
    expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected
