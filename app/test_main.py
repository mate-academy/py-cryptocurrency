from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, expected_rate, expected_result",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 100.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
        (100, 95.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
    current_rate: int | float,
    expected_rate: int | float,
    expected_result: str,

) -> None:
    mocked_get_exchange_rate_prediction.return_value = expected_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
