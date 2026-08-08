import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate,expected",
    [
        (50, "Sell all your cryptocurrency"),
        (150, "Buy more cryptocurrency"),
        (95, "Do nothing"),
        (105, "Do nothing"),
    ],
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction: mock.MagicMock,
        current_rate: int,
        expected: str
) -> None:
    get_exchange_rate_prediction.return_value = current_rate
    assert cryptocurrency_action(100) == expected
