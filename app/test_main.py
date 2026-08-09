from unittest import mock
from typing import Union
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 110, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (10, 10.51, "Buy more cryptocurrency"),
        (10, 9.49, "Sell all your cryptocurrency"),
    ]
)
def test_cryptocurrency_action(
    current_rate: Union[int, float],
    prediction_rate: Union[int, float],
    expected: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction"
    ) as mocked_prediction:
        mocked_prediction.return_value = prediction_rate

        result = cryptocurrency_action(current_rate)

        assert result == expected
