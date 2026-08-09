import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 105.0, "Do nothing"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 95.0, "Do nothing"),
        (100, 100, "Do nothing"),
    ],
    ids=[
        "more_than_5_percent_higher",
        "exactly_5_percent_higher",
        "more_than_5_percent_lower",
        "exactly_5_percent_lower",
        "no_change"
    ]
)
def test_cryptocurrency_action(
    current_rate: float,
    predicted_rate: float,
    expected_action: str
) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mocked_prediction:
        mocked_prediction.return_value = predicted_rate

        assert cryptocurrency_action(current_rate) == expected_action
