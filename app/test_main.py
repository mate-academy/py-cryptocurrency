from unittest import mock
from unittest.mock import Mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (10.5, 20, "Buy more cryptocurrency"),
        (10, 4.2, "Sell all your cryptocurrency"),
        (10, 10, "Do nothing"),
        (10, 10.5, "Do nothing"),
        (10, 9.5, "Do nothing"),
    ],
    ids=[
        "test_buy_when_prediction_higher",
        "test_sell_when_prediction_lower",
        "test_do_nothing_when_equal",
        "test_do_nothing_when_rate_is_exactly_105_percent",
        "test_do_nothing_when_rate_is_exactly_95_percent"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_exchange_rate_prediction: Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    mock_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
    mock_exchange_rate_prediction.assert_called_once()
