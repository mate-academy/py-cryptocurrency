import pytest
from unittest import mock
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate, result",
    [
        (0.9, "Sell all your cryptocurrency"),
        (0.95, "Do nothing"),
        (1, "Do nothing"),
        (1.05, "Do nothing"),
        (1.1, "Buy more cryptocurrency")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_test_cryptocurrency_action_(mocked_get_exchange: mock,
                                     rate: int | float,
                                     result: str) -> None:

    mocked_get_exchange.return_value = rate
    assert cryptocurrency_action(1) == result
