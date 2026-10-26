from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected",
    [
        (100, 200, "Buy more cryptocurrency"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 105.01, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 104, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 96, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 1, "Sell all your cryptocurrency"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_prediction: mock.MagicMock,
    current_rate: float,
    predicted_rate: float,
    expected: str,
) -> None:
    mocked_prediction.return_value = predicted_rate

    assert cryptocurrency_action(current_rate) == expected
    mocked_prediction.assert_called_once_with(current_rate)
# write your code here
