from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_action",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (1, 1.2, "Buy more cryptocurrency"),
        (1, 0.8, "Sell all your cryptocurrency"),
    ],
    ids=[
        "more than 5% higher: buy",
        "exactly 5% higher: do nothing",
        "same rate: do nothing",
        "exactly 5% lower: do nothing",
        "more than 5% lower: sell",
        "small rate, much higher: buy",
        "small rate, much lower: sell",
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_prediction: mock.MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected_action: str,
) -> None:
    mocked_prediction.return_value = predicted_rate

    assert main.cryptocurrency_action(current_rate) == expected_action
