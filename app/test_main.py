from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,message",
    [
        pytest.param(
            100,
            150,
            "Buy more cryptocurrency",
            id="Predict exchange rate is more than 5% higher"
        ),
        pytest.param(
            100,
            50,
            "Sell all your cryptocurrency",
            id="Predict exchange rate is more than 5% lower"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="You should not sell cryptocurrency"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="You should not buy cryptocurrency"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_return_correct_message(
        mock_exchange,
        current_rate,
        exchange_rate,
        message
):
    mock_exchange.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == message
