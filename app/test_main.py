from unittest.mock import patch
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        pytest.param(100, 106, "Buy more cryptocurrency",
                     id="more_than_105"),
        pytest.param(100, 94, "Sell all your cryptocurrency",
                     id="less_than_95"),
        pytest.param(100, 105, "Do nothing", id="exactly_105"),
        pytest.param(100, 95, "Do nothing", id="exactly_95"),
        pytest.param(100, 100, "Do nothing", id="same_rate"),
    ],
)
def test_cryptocurrency_action(
    current_rate: int,
    predicted_rate: int,
    expected: str,
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        result = cryptocurrency_action(current_rate)

    assert result == expected
