import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.fixture
def mock_get_exchange_rate_prediction() -> mock.Mock:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_func:
        yield mock_func


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100, 104, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
def test_cryptocurrency_action(
        current_rate: float, predicted_rate: float, expected_action: str,
        mock_get_exchange_rate_prediction: mock.Mock
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_action, (
        f"Expected action: '{expected_action}', "
        f"but got: '{cryptocurrency_action(current_rate)}'"
    )
