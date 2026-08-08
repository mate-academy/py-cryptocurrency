import pytest
from unittest import mock
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        (1, 2, "Buy more cryptocurrency"),
        (2, 1, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
    ],
    ids=[
        "should return 'Buy more cryptocurrency' with current=1, expected=2",
        "should return 'Sell all your cryptocurrency' "
        "with current=2, expected=1",
        "should return 'Do nothing' with current=1, expected=1",
        "should return 'Do nothing' with current=1, expected=1.05",
        "should return 'Do nothing' with current=1, expected=0.95",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
    current_rate: Union[int, float],
    prediction_rate: Union[int, float],
    expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_result
