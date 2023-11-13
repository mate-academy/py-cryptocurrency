from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, expected_rate, expected",
    [
        (1, 1.6,  "Buy more cryptocurrency"),
        (1, 0.6,  "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: float,
        current_rate: int | float,
        expected_rate: int | float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = expected_rate

    assert cryptocurrency_action(current_rate) == expected
