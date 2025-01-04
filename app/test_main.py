import pytest
from app.main import cryptocurrency_action
from typing import Union
from unittest import mock


@pytest.mark.parametrize(
    "current_rate,prediction_rate,action",
    [
        (100, 115, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 97, "Do nothing")
    ]
)
def test_cryptocurrency_action_works_correctly(
        current_rate: Union[int, float],
        prediction_rate: Union[int, float],
        action: str,
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_rate_prediction):
        mocked_rate_prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == action
