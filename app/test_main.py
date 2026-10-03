from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, expected_result",
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    prediction_rate: float,
    expected_result: str,
) -> None:
    current_rate = 100

    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction_rate,
    ):
        result = cryptocurrency_action(current_rate)

    assert result == expected_result
