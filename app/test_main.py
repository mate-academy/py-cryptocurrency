from unittest.mock import MagicMock, patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 103, "Do nothing"),
        (100, 97, "Do nothing"),
    ],
    ids=[
        "buy_action",
        "sell_action",
        "do_nothing_equal",
        "boundary_105_do_nothing",
        "boundary_95_do_nothing",
        "do_nothing_slight_increase",
        "do_nothing_slight_decrease",
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mock_get_prediction: MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    mock_get_prediction.return_value = predicted_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected


def test_cryptocurrency_action_returns_str() -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=100
    ):
        result = cryptocurrency_action(100)
        assert isinstance(result, str)
