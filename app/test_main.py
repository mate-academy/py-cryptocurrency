import pytest
from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate,current_rate,returned_string",
    [
        (1, 1, "Do nothing"),
        (833.9, 132, "Buy more cryptocurrency"),
        (34.2, 122.4, "Sell all your cryptocurrency"),
        (190, 200, "Do nothing"),
        (210, 200, "Do nothing")
    ]
)
def test_should_take_exchange_rate(
        mocked_prediction: MagicMock,
        prediction_rate: float | int,
        current_rate: float | int,
        returned_string: str
) -> None:
    mocked_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == returned_string
