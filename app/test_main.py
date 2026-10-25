from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("current_rate", "predicted_rate", "expected_action"),
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
        current_rate: int,
        predicted_rate: int,
        expected_action: str,
) -> None:
    with patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ) as prediction_mock:
        assert cryptocurrency_action(current_rate) == expected_action

    prediction_mock.assert_called_once_with(current_rate)
