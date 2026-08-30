from unittest import mock
from unittest.mock import MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "get_exchange_rate_prediction_result, current_rate, expected",
    [
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (100, 100, "Do nothing"),
        (95.2, 109.3, "Sell all your cryptocurrency"),
        (147.68, 54.26, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: MagicMock,
        get_exchange_rate_prediction_result: int | float,
        current_rate: int | float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value =\
        get_exchange_rate_prediction_result
    assert cryptocurrency_action(current_rate) == expected
