import pytest

from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predict_rate, action",
    [
        (1000, 1100, "Buy more cryptocurrency"),
        (1100, 1000, "Sell all your cryptocurrency"),
        (1010, 1000, "Do nothing"),
        (1000, 950, "Do nothing"),
        (1000, 1050, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_action(
        mock_rate: mock,
        current_rate: int,
        predict_rate: int,
        action: str
) -> None:
    mock_rate.return_value = predict_rate
    assert cryptocurrency_action(current_rate) == action
