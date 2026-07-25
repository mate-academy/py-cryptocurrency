import pytest
from unittest.mock import patch, MagicMock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, expected",
    [
        (94.99, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (100, "Do nothing"),
        (105, "Do nothing"),
        (105.01, "Buy more cryptocurrency"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_return_correct_value(
        mocked_get_exchange_rate_prediction: MagicMock,
        prediction_rate: int | float,
        expected: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(100) == expected
