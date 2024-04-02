import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected",
    [
        (100, 1000, "Sell all your cryptocurrency"),
        (1050, 1000, "Do nothing"),
        (950, 1000, "Do nothing"),
        (1150, 1000, "Buy more cryptocurrency"),
        (900, 1000, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    prediction_rate: float,
    current_rate: float,
    expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
