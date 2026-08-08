import pytest
from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate,rate_prediction,expected",
    [
        pytest.param(
            10,
            10 * 1.6,
            "Buy more cryptocurrency",
            id="more than 5% higher from the current"
        ),
        pytest.param(
            10,
            10 * 0.94,
            "Sell all your cryptocurrency",
            id="more than 5% lower from the current"
        ),
        pytest.param(
            10,
            10 * 1.05,
            "Do nothing",
            id="difference in range of 5%"
        ),
        pytest.param(
            10,
            10 * 0.95,
            "Do nothing",
            id="difference in range of 5%"
        )
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(get_exchange_rate_prediction: MagicMock,
                               rate: int | float, rate_prediction: int | float,
                               expected: str) -> None:
    get_exchange_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(rate) == expected
