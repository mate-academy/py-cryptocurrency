import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 103, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_all_crypto_situation(mock_prediction: int, current_rate: int,
                              predicted_rate: int, expected: int) -> None:
    mock_prediction.return_value = predicted_rate

    result = cryptocurrency_action(current_rate)

    assert result == expected
