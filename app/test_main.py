import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, expected_rate, message",
    [
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: int | float,
        current_rate: int | float,
        expected_rate: int | float,
        message: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = expected_rate

    assert cryptocurrency_action(current_rate) == message
