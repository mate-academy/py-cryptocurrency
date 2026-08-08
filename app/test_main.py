from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_prediction,current_rate,expected_result",
    [
        pytest.param(
            40,
            20,
            "Buy more cryptocurrency",
            id="Buy if exchange rate is more than 5% higher "
        ),
        pytest.param(
            20,
            25,
            "Sell all your cryptocurrency",
            id="Sell if exchange rate is more than 5% lower"
        ),
        pytest.param(
            19.0,
            20.0,
            "Do nothing",
            id="No action if difference is 0.95"
        ),
        pytest.param(
            21,
            20.0,
            "Do nothing",
            id="No action if difference is 1.05"
        ),
    ]
)
def test_cryptocurrency_return_correct_prediction(
        rate_prediction: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = rate_prediction
        assert cryptocurrency_action(current_rate) == expected_result
