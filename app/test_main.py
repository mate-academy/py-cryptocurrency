import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_prediction, expected_result",
    [
        (106.0, "Buy more cryptocurrency"),
        (94.0, "Sell all your cryptocurrency"),
        (101.0, "Do nothing"),
        (105.0, "Do nothing"),
        (95.0, "Do nothing"),
    ],
    ids=[
        "Predicted more than 5% increase",
        "Predicted more than 5% decrease",
        "Prediction is to wait",
        "Prediction is to wait",
        "Prediction is to wait",
    ]
)
def test_cryptocurrency_action(
        exchange_prediction: mock.MagicMock,
        expected_result: mock.MagicMock
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=exchange_prediction
    ):
        assert cryptocurrency_action(100) == expected_result
