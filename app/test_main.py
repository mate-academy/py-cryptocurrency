import pytest
from unittest import mock
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_currency, prediction_currency, expected",
    [
        (110, 100.00, "Sell all your cryptocurrency"),
        (80, 100.00, "Buy more cryptocurrency"),
        (100, 95.00, "Do nothing"),
        (100, 105.00, "Do nothing"),
        (100, 100.00, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mock_prediction: mock.Mock,
        current_currency: int | float,
        prediction_currency: int | float,
        expected: str) -> None:
    mock_prediction.return_value = prediction_currency
    assert cryptocurrency_action(current_currency) == expected
