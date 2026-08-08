import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    ("mock_return_value", "current_rate", "expected"),
    [
        (15, 20, "Sell all your cryptocurrency"),
        (19, 20, "Do nothing"),
        (20, 15, "Buy more cryptocurrency"),
        (105, 100, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        get_exchange_rate_prediction: mock.MagicMock,
        mock_return_value: int,
        current_rate: int | float,
        expected: str,
) -> None:
    get_exchange_rate_prediction.return_value = mock_return_value
    assert cryptocurrency_action(current_rate) == expected
