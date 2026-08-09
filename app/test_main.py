from unittest.mock import patch

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, current, result",
    [
        (100, 50, "Buy more cryptocurrency"),
        (52, 51, "Do nothing"),
        (48, 50, "Do nothing"),
        (25, 60, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
    ],
    ids=[
        "prediction is much bigger",
        "prediction is a bit bigger",
        "prediction is a bit lower",
        "prediction is much lower",
        "prediction to current is 1.05",
        "prediction to current is 0.95",
    ]
)
def test_cryptocurrency_action(
        prediction: int | float,
        current: int | float,
        result: str,
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = prediction
        assert cryptocurrency_action(current) == result
