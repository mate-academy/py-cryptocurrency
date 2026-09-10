from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (1, 1, "Do nothing"),
        (1.06, 1, "Buy more cryptocurrency"),
        (0.94, 1, "Sell all your cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange: mock.MagicMock,
        prediction_rate: float | int,
        current_rate: float | int,
        expected_result: str,
) -> None:
    mock_get_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
