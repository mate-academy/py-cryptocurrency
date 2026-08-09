from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_result",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94.99, "Sell all your cryptocurrency")
    ],
    ids=[
        ("should return 'Buy more cryptocurrency' when predicted rate "
         "to current rate is greater than 1.05"),
        ("should return 'Do nothing' when predicted rate "
         "to current rate is not greater than 1.05"),
        ("should return 'Do nothing' when predicted rate "
         "to current rate is greater than 0.95"),
        ("should return 'Sell all your cryptocurrency' when predicted rate "
         "to current rate is smaller than 0.95")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_prediction: mock.MagicMock,
        current_rate: int | float,
        predicted_rate: int | float,
        expected_result: str
) -> None:
    mock_get_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == expected_result
