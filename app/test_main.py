from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "positive, negative, solution",
    [
        pytest.param(
            1, 1.05, "Do nothing",
            id="no changes"
        ),
        pytest.param(
            1, 0.7, "Sell all your cryptocurrency",
            id="negative_prediction"
        ),
        pytest.param(
            1, 1.2, "Buy more cryptocurrency",
            id="positive_prediction"
        ),
        pytest.param(
            1, 0.95, "Do nothing", id="positive_prediction"
        )
    ]
)
def test_cryptocurrency_action(
        positive: int,
        negative: int | float,
        solution: str
) -> None:

    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mocked_prediction
    ):
        mocked_prediction.return_value = negative
        result = cryptocurrency_action(current_rate=positive)
        assert result == solution, (
            f"Expected result to be {solution}, "
            f"But got {result}"
        )
