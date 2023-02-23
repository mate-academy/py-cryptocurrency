from unittest import mock
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate, result",
    [
        pytest.param(1.15, "Buy more cryptocurrency", id="rate > 1.05"),
        pytest.param(0.85, "Sell your cryptocurrency", id="rate less 0.95"),
        pytest.param(0.95, "Do nothing", id="should do nothing"),
        pytest.param(1.05, "Do nothing", id="should do nothing")

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate: mock,
        rate: float,
        result: str
) -> None:
    mocked_exchange_rate.return_value = rate
    assert cryptocurrency_action(1.0) == result
