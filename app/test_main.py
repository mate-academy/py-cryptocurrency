import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, mocked_value, result", [
        pytest.param(100, 106, "Buy more cryptocurrency",
                     id="Predicted rate is 6% higher"),
        pytest.param(100, 94, "Sell all your cryptocurrency",
                     id="Predicted rate is 6% lower"),
        pytest.param(100, 102, "Do nothing",
                     id="Predicted rate is within 5% difference"),
        pytest.param(100, 95, "Do nothing",
                     id="Predicted rate is 5%"),
        pytest.param(100, 105, "Do nothing",
                     id="Predicted rate is 5%")
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        mocked_value: int | float,
        result: str) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mocked_get_exchange_rate_prediction):
        mocked_get_exchange_rate_prediction.return_value = mocked_value
        assert cryptocurrency_action(current_rate) == result
