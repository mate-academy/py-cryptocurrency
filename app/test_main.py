from unittest.mock import Mock, patch

import pytest

from app.main import cryptocurrency_action

Number = int | float


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 150, "Buy more cryptocurrency"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 50, "Sell all your cryptocurrency"),
    ],
    ids=[
        "prediction is more greater than 5 percents",
        "prediction is greater than 5 percents",
        "prediction is 5 percents",
        "prediction is 0 percents",
        "prediction is -5 percents",
        "prediction is less than -5 percents",
        "prediction is more less than -5 percents"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_prediction: Mock,
        current_rate: Number,
        prediction_rate: Number,
        expected: str
) -> None:
    mock_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
