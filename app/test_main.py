import pytest

from unittest import mock

import app.main


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 0, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (200, 210, "Do nothing")
    ]
)
def test_cryptocurrency_action(current_rate: int,
                               predicted_rate: int,
                               expected: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_function):
        mocked_function.return_value = predicted_rate
        assert app.main.cryptocurrency_action(current_rate) == expected
