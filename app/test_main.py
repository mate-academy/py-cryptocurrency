import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate,percent,expected_value",
    [
        (100, 105, "Do nothing"),
        (100, 120, "Buy more cryptocurrency"),
        (100, 101, "Do nothing"),
        (100, 78, "Sell all your cryptocurrency"),
        (100, 114, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 99, "Do nothing"),
        (100, 109, "Buy more cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto(
        mock_function: mock,
        current_rate: int,
        percent: int,
        expected_value: str
) -> None:
    mock_function.return_value = percent
    assert cryptocurrency_action(current_rate) == expected_value
