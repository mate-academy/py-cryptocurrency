import pytest
from unittest.mock import patch, MagicMock
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mocked_predict, expected_action",
    [
        (2, 3, "Buy more cryptocurrency"),
        (5, 4, "Sell all your cryptocurrency"),
        (4.9, 5, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
    ids=[
        "predict more than current rate",
        "predict less than current rate",
        "predict equal current rate",
        "predict exactly 5% increase boundary",
        "predict exactly 5% decrease boundary"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: MagicMock,
    current_rate: Union[int, float],
    mocked_predict: Union[int, float],
    expected_action: str
) -> None:
    mock_prediction.return_value = mocked_predict

    result = cryptocurrency_action(current_rate)

    assert result == expected_action
