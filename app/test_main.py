from unittest import mock
import pytest
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize("current_rate, prediction_rate, expected", [
    (100, 110, "Buy more cryptocurrency"),
    (100, 90, "Sell all your cryptocurrency"),
    (100, 100, "Do nothing"),
])
def test_cryptocurrency_action(
        mock_prediction: mock.MagicMock,
        current_rate: int,
        prediction_rate: int,
        expected: str
) -> None:
    mock_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected
    mock_prediction.assert_called_once_with(current_rate)
