import pytest
from unittest import mock
from typing import Union

import app.main


@pytest.mark.parametrize(
    "current_exchange_rate,predicted_exchange_rate,expected_result",
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
def test_cryptocurrency_action(
    mocked_get_exchange_rate_prediction: mock.MagicMock,
    current_exchange_rate: Union[int, float],
    predicted_exchange_rate: Union[int, float],
    expected_result: str
) -> None:
    mocked_get_exchange_rate_prediction.return_value = predicted_exchange_rate

    assert (expected_result
            == app.main.cryptocurrency_action(current_exchange_rate))
