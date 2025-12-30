import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "exchange_rate,current_rate,expected_output",
    [
        (0.93, 1, "Sell all your cryptocurrency"),
        (1.06, 1, "Buy more cryptocurrency"),
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
    ],
    ids=[
        "test current rate is higher than 5%",
        "test current rate is lower than 5%",
        "test current rate is equally 5% lower",
        "test current rate is equally 5% higher"
    ]
)
def test_cryptocurrency_action(
        exchange_rate: int,
        current_rate: int,
        expected_output: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_exchange_rate):
        mock_exchange_rate.return_value = exchange_rate
        assert cryptocurrency_action(current_rate) == expected_output
