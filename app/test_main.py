from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (8, 7.16, "Sell all your cryptocurrency"),
        (2, 11.21, "Buy more cryptocurrency"),
        (0.7, 0.73, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_rate_prediction,
        current_rate: int|float,
        prediction_rate: int|float,
        result: str
) -> None:
    mock_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result