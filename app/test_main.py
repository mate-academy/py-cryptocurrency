import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_return, current, expected",
    [
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing"),
        (106, 100, "Buy more cryptocurrency"),
        (94, 100, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_scenario(
        mock_exchange: int,
        mock_return: int,
        current: int,
        expected: str
) -> None:
    mock_exchange.return_value = mock_return
    assert cryptocurrency_action(current) == expected
