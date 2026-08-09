import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate, current_rate, expected",
    [
        (110, 100, "Buy more cryptocurrency"),
        (90, 100, "Sell all your cryptocurrency"),
        (101, 100, "Do nothing"),
        (99, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")

    ],
    ids=[
        "Predicted more than 5% higher should result Buy all",
        "Predicted more than 5% lower should result Sell all",
        "Predicted less than 5% higher should result  Do nothing",
        "Predicted less than 5% lower should result Do nothing",
        "Predicted 5% higher should result Do nothing",
        "Predicted 5% lower should result Do nothing"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_rate: int | float,
        predicted_rate: int | float,
        current_rate: int | float,
        expected: str) -> None:
    mocked_get_rate.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected
