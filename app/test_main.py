import pytest
from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "initial_value_return,expected_result",
    [
        (10.51, "Buy more cryptocurrency"),
        (9.49, "Sell all your cryptocurrency"),
        (10.50, "Do nothing"),
        (9.50, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_exchange_rate_prediction: MagicMock,
    initial_value_return: float,
    expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = initial_value_return
    assert cryptocurrency_action(10) == expected_result
