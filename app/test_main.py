import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (1, 1, "Do nothing"),
        (1, 1.05, "Do nothing"),
        (1, 0.95, "Do nothing"),
        (1, 156, "Buy more cryptocurrency"),
        (1, 0.72, "Sell all your cryptocurrency"),
        # (100, 106, "Buy more cryptocurrency"),
        # (100, 105, "Do nothing"),
        # (100, 95, "Do nothing"),
        # (100, 94, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_func: callable,
    current_rate: float,
    prediction_rate: float,
    expected_action: str,
) -> None:
    mock_func.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_action
