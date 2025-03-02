import pytest
from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, expected",
    [
        (106, "Buy more cryptocurrency"),  # >5% більше
        (94, "Sell all your cryptocurrency"),  # >5% менше
        (95, "Do nothing"),  # Межа -5%
        (105, "Do nothing"),  # Межа +5%
        (100, "Do nothing"),  # Без змін
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_prediction: Mock,
    predicted_rate: int,
    expected: str
) -> None:

    mock_get_prediction.return_value = predicted_rate
    assert cryptocurrency_action(100) == expected
