import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_action",
    [
        (100.0, 105.1, "Buy more cryptocurrency"),
        (100.0, 120.0, "Buy more cryptocurrency"),
        (100.0, 94.9, "Sell all your cryptocurrency"),
        (100.0, 80.0, "Sell all your cryptocurrency"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 95.0, "Do nothing"),
        (100.0, 100.0, "Do nothing"),
        (100.0, 104.0, "Do nothing"),
        (100.0, 96.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_prediction: mock.MagicMock,
    current_rate: float,
    prediction_rate: float,
    expected_action: str
) -> None:
    mock_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
    mock_prediction.assert_called_once_with(current_rate)
