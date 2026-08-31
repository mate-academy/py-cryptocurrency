import pytest

from unittest import mock
from unittest.mock import MagicMock

from app import main


@pytest.mark.parametrize(
    "get_exchange_rate_prediction_result, current_rate, expected",
    [
        (109, 100, "Buy more cryptocurrency"),
        (153.94, 48.39, "Buy more cryptocurrency"),
        (23, 92, "Sell all your cryptocurrency"),
        (75.57, 165.85, "Sell all your cryptocurrency"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (50, 50, "Do nothing"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_get_exchange_rate_prediction: MagicMock,
        get_exchange_rate_prediction_result: int | float,
        current_rate: int | float,
        expected: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value =\
        get_exchange_rate_prediction_result
    assert main.cryptocurrency_action(current_rate) == expected
