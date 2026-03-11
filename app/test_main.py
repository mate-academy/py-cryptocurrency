from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predict,curr,expected",
    [
        (100, 50, "Buy more cryptocurrency"),
        (50, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action(
        predict: int,
        curr: int,
        expected: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=predict
    ):
        assert cryptocurrency_action(curr) == expected
