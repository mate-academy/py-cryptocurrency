from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,exchange_rate,result",
    [
        pytest.param(
            1, 1, "Do nothing",
            id="No change predicted, do nothing"),
        pytest.param(
            1, 1.05, "Do nothing",
            id="Small change predicted, do nothing"),
        pytest.param(
            1, 0.95, "Do nothing",
            id="Small change predicted, do nothing"),
        pytest.param(
            1, 1.06, "Buy more cryptocurrency",
            id="predicted rate is high, Buy more cryptocurrency"),
        pytest.param(
            1, 0.5, "Sell all your cryptocurrency",
            id="predicted rate is low, Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_if_inner_function_call(
        mocked_get_exchange_rate_prediction: mock.MagicMock,
        current_rate: int | float,
        exchange_rate: int | float,
        result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = exchange_rate
    assert cryptocurrency_action(current_rate) == result
