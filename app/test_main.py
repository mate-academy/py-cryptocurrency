import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected_result",
    [
        pytest.param(
            10.6, 10, "Buy more cryptocurrency",
            id="if exchange rate is more than 5% higher from the current"
        ),
        pytest.param(
            9.4, 10, "Sell all your cryptocurrency",
            id="if exchange rate is more than 5% lower from the current"
        ),
        pytest.param(
            10.5, 10, "Do nothing",
            id="if difference is not that much, upper edge"
        ),
        pytest.param(
            9.5, 10, "Do nothing",
            id="if difference is not that much, lower edge"
        ),
    ]
)
def test_cryptocurrency_action(
        prediction_rate: float,
        current_rate: int,
        expected_result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        assert cryptocurrency_action(current_rate) == expected_result
