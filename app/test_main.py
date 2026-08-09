import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predict_rate, action",
    [
        (100, 110, "Buy more cryptocurrency"),
        (110, 100, "Sell all your cryptocurrency"),
        (101, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
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
