from app.main import cryptocurrency_action

import pytest

from unittest import mock


@pytest.mark.parametrize(
    "predict_rate,current_rate,expected_value",
    [
        (1.06, 1.0, "Buy more cryptocurrency"),
        (0.92, 1.0, "Sell all your cryptocurrency"),
        (1.01, 1.0, "Do nothing"),
        (0.95, 1.0, "Do nothing"),
        (1.05, 1.0, "Do nothing"),
    ],
)
def test_cryptocurrency_action(
        predict_rate: float,
        current_rate: float,
        expected_value: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mock_rate_pred:
        mock_rate_pred.return_value = predict_rate

        assert cryptocurrency_action(current_rate) == expected_value
