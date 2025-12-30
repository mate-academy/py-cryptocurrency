import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, predicted_rate, result",
    [
        pytest.param(
            100,
            200,
            "Buy more cryptocurrency",
            id="predicted exchange rate is more than 5% higher"
        ),
        pytest.param(
            200,
            100,
            "Sell all your cryptocurrency",
            id="predicted exchange rate is more than 5% lower"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="difference is not that much"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="difference is not that much"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_crypto_action_result(
        mocked_exchange_rate_prediction: callable,
        current_rate: float,
        predicted_rate: float,
        result: str
) -> None:
    mocked_exchange_rate_prediction.return_value = predicted_rate
    assert cryptocurrency_action(current_rate) == result
