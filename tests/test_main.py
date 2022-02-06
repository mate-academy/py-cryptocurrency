from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "initial_value,expected_prediction",
    [
        (
            1050,
            "Do nothing"
        ),
        (
            1000,
            "Sell all your cryptocurrency"
        ),
        (
            1100,
            "Buy more cryptocurrency"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_rate_prediction(mocked_get_exchange, initial_value, expected_prediction):
    mocked_get_exchange.return_value = initial_value

    assert cryptocurrency_action(1000) == expected_prediction
