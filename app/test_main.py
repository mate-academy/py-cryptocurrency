import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "curr_rate", "prediction", "result",
    [
        pytest.param(1, 1.06, "Buy more cryptocurrency"),
        pytest.param(2, 1, "Sell all your cryptocurrency"),
        pytest.param(4, 4, "Do nothing"),
        pytest.param(100, 96, "Do nothing"),
        pytest.param(100, 94, "Do nothing"),
        pytest.param(1, 0.95, "Do nothing"),
        pytest.param(1, 1.05,  "Do nothing")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_rate(
        mocked_function: mock,
        curr_rate: int | float,
        prediction: int | float,
        result: str
) -> None:
    mocked_function.return_value = prediction
    assert cryptocurrency_action(curr_rate) == result
