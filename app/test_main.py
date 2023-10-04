import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,action",
    [
        pytest.param(
            100,
            100,
            "Do nothing",
            id="Should not offer any action without changes"
        ),
        pytest.param(
            100,
            200,
            "Buy more cryptocurrency",
            id="Offers to invest if the rate increases >5%"
        ),
        pytest.param(
            200,
            100,
            "Sell all your cryptocurrency",
            id="Offers to sell if the rate decreases >5%"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="No offer if the rate increases <5%"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="No offer if the rate decreases <5%"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_currency_return_values(
        mocked_exchange: callable,
        current_rate: int,
        predicted_rate: int,
        action: str
) -> None:
    mocked_exchange.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == action
