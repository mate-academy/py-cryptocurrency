import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize("current_rate, predicted_rate, expected", [
    (100, 106, "Buy more cryptocurrency"),
    (100, 94, "Sell all your cryptocurrency"),
    (100, 100, "Do nothing"),
    (100, 105, "Do nothing"),
    (100, 95, "Do nothing"),
])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_exchange_rate_prediction: mock.MagicMock,
                               current_rate: int,
                               predicted_rate: int,
                               expected: str) -> None:
    mock_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
    mock_exchange_rate_prediction.assert_called_once_with(current_rate)
