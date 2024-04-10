from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate: mock.MagicMock,
        current_rate: int,
        prediction_rate: float,
        expected: str
) -> None:
    mocked_get_exchange_rate.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected
