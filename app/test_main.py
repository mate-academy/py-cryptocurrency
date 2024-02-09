import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("current_rate", "prediction", "expected_result"),
    [
        (0.95, 1.0, "Buy more cryptocurrency"),
        (1.4, 1.1, "Sell all your cryptocurrency"),
        (1.05, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing"),
        (1.0, 1.0, "Do nothing"),
        (1.0, 1.1, "Sell all your cryptocurrency"),
    ],
    ids=[
        "Should return 'Buy more cryptocurrency' when prediction > 1.05",
        "Should return 'Sell all your cryptocurrency' when prediction < 0.95",
        "Should return 'Do nothing' when prediction is 1.05",
        "Should return 'Do nothing' when prediction is less than 0.95",
        "Should return 'Do nothing' when prediction is exactly 1.0",
        "Should return 'Sell all your cryptocurrency' when prediction > 1.05",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_exchange: mock,
    current_rate: int | float,
    prediction: int | float,
    expected_result: str
) -> None:
    mock_exchange.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
