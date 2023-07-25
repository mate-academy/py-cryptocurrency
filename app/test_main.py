from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (10, 10.5, "Do nothing"),
        (10.0, 9.5, "Do nothing"),
        (10, 11.5, "Buy more cryptocurrency"),
        (10.0, 7, "Sell all your cryptocurrency"),
    ],
    ids=[
        "10 / 10.5 should return  'Do nothing'",
        "10.0 / 9.5 should return  'Do nothing'",
        "10 / 11.5 should return  'Buy more cryptocurrency'",
        "10.0 / 7 should return  'Sell all your cryptocurrency'"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: int | float,
        prediction_rate: float,
        expected: str,
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected
