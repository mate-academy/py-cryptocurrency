import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_rate, expected_result",
    [
        (110, "Buy more cryptocurrency"),
        (90, "Sell all your cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange: mock.MagicMock,
        mock_rate: int | float,
        expected_result: str
) -> None:
    mocked_exchange.return_value = mock_rate
    assert cryptocurrency_action(100) == expected_result
