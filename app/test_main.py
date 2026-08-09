import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.fixture
def mocked_prediction() -> MagicMock:
    with patch("app.main.get_exchange_rate_prediction") as mock:
        yield mock


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100.0, 95.0, "Do nothing"),
        (100.0, 105.0, "Do nothing"),
        (100.0, 106.0, "Buy more cryptocurrency"),
        (100.0, 94.0, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    predicted_rate: float,
    expected_result: str,
    mocked_prediction: MagicMock,
) -> None:

    mocked_prediction.return_value = predicted_rate
    result: str = cryptocurrency_action(current_rate)
    assert result == expected_result
