import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "current_rate, prediction, expected_result",
    [
        pytest.param(
            1, 1.06, "Buy more cryptocurrency",
            id="profit more than 5% higher from the current"
        ),
        pytest.param(
            1, 0.94, "Sell all your cryptocurrency",
            id="profit more than 5% lower from the current"
        ),
        pytest.param(
            1, 1, "Do nothing",
            id="profit 0%"
        ),
        pytest.param(
            1, 1.05, "Do nothing",
            id="profit < 5%"
        ),
        pytest.param(
            1, 0.95, "Do nothing",
            id="loss < 5%"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mocked_prediction: callable,
                               current_rate: int | float,
                               prediction: float,
                               expected_result: str) -> None:
    mocked_prediction.return_value = prediction
    assert cryptocurrency_action(current_rate) == expected_result
