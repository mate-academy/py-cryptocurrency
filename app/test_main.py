from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    with mock.patch.object(
        main, "get_exchange_rate_prediction", return_value=predicted_rate
    ):
        result = main.cryptocurrency_action(current_rate)

    assert result == expected
