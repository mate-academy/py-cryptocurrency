import pytest

from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 102, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mocked_get_exchange_rate_prediction: MagicMock,
        current_rate: int,
        prediction_rate: int,
        expected: str,
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
