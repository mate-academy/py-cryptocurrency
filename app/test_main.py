from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate_prediction,expected_result",
    [
        pytest.param(
            100,
            106,
            "Buy more cryptocurrency",
            id="should recommend to buy more if rate more than 5% higher"
        ),
        pytest.param(
            100,
            94,
            "Sell all your cryptocurrency",
            id="should recommend to sell if rate more than 5% lower"
        ),
        pytest.param(
            100,
            105,
            "Do nothing",
            id="should recommend to do nothing if less than 5% higher"
        ),
        pytest.param(
            100,
            95,
            "Do nothing",
            id="should recommend to do nothing if less than 5% lower"
        )
    ]
)
def test_cryptocurrency_action_different_scenarios(
        current_rate: int,
        exchange_rate_prediction: int,
        expected_result: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_prediction):
        mock_prediction.return_value = exchange_rate_prediction
        assert cryptocurrency_action(current_rate) == expected_result
