from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 200, "Buy more cryptocurrency"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 0, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    predicted_rate: float,
    expected: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=predicted_rate,
    ):
        assert main.cryptocurrency_action(current_rate) == expected


def test_prediction_should_be_requested_with_current_rate() -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=100,
    ) as mocked_prediction:
        main.cryptocurrency_action(100)
        mocked_prediction.assert_called_once_with(100)
