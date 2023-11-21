from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, future_rate, expected_result",
    [
        (100, 102.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 98.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
        (100, 106.0, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_rate: mock.MagicMock,
        current_rate: int | float,
        future_rate: int | float,
        expected_result: str
) -> None:
    mock_get_rate.return_value = future_rate
    assert cryptocurrency_action(current_rate) == expected_result
