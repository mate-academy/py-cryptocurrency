import pytest

from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "get_exchange_rate, current_rate, expected_result",
    [
        (82.6, 5, "Buy more cryptocurrency"),
        (2.4, 5, "Sell all your cryptocurrency"),
        (5.25, 5, "Do nothing"),
        (4.75, 5, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: pytest.param,
        get_exchange_rate: float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = get_exchange_rate
    assert cryptocurrency_action(current_rate) == expected_result
