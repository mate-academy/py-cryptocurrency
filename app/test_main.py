from unittest import mock

import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        pytest.param(
            100, 106, "Buy more cryptocurrency",
            id="should buy when rate grows more than 5%"
        ),
        pytest.param(
            100, 94, "Sell all your cryptocurrency",
            id="should sell when rate falls more than 5%"
        ),
        pytest.param(
            100, 100, "Do nothing",
            id="should do nothing when rate does not change"
        ),
        pytest.param(
            100, 105, "Do nothing",
            id="should do nothing when rate grows exactly 5%"
        ),
        pytest.param(
            100, 95, "Do nothing",
            id="should do nothing when rate falls exactly 5%"
        ),
    ]
)
def test_cryptocurrency_action(
        current_rate: int | float,
        prediction_rate: int | float,
        expected: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction_rate
    ) as mocked_prediction:
        assert main.cryptocurrency_action(current_rate) == expected
        mocked_prediction.assert_called_once_with(current_rate)
