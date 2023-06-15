from unittest.mock import patch
from typing import Any

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_crypto_behavior(mocked_get_exchange_rate_prediction: Any) -> str:
    mocked_get_exchange_rate_prediction.return_value = 0.7
    assert cryptocurrency_action(0.5) == "Buy more cryptocurrency"

    mocked_get_exchange_rate_prediction.return_value = 0.3
    assert cryptocurrency_action(0.5) == "Sell all your cryptocurrency"

    mocked_get_exchange_rate_prediction.return_value = 0.475
    assert cryptocurrency_action(0.5) == "Do nothing"

    mocked_get_exchange_rate_prediction.return_value = 0.525
    assert cryptocurrency_action(0.5) == "Do nothing"
