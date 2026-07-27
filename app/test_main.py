import pytest
from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (1.25, 1.50, "Buy more cryptocurrency"),
        (1.01, 0.88, "Sell all your cryptocurrency"),
        (1.75, 1.77, "Do nothing"),
        (1, 1, "Do nothing"),
        (2, 1.9, "Do nothing"),
        (5, 5.25, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange: MagicMock,
        current_rate: float | int,
        prediction_rate: float | int,
        expected: str
) -> None:
    mock_get_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected

    mock_get_exchange.assert_called_once_with(current_rate)
