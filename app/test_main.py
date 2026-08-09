from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,expected_action",
    [
        pytest.param(
            1000, 1051, "Buy more cryptocurrency",
            id="predicted rate is more than 5% higher",
        ),
        pytest.param(
            1000, 949, "Sell all your cryptocurrency",
            id="predicted rate is more than 5% lower",
        ),
        pytest.param(
            1000, 1050, "Do nothing",
            id="predicted rate is not exceed 5% bounds",
        ),
        pytest.param(
            1000, 950, "Do nothing",
            id="predicted rate is not exceed 5% bounds",
        ),
    ]
)
def test_cryptocurrency_action(
        current_rate: float,
        predicted_rate: float,
        expected_action: str
) -> None:
    with (
        mock.patch("app.main.get_exchange_rate_prediction")
        as mock_prediction
    ):
        mock_prediction.return_value = predicted_rate

        assert cryptocurrency_action(current_rate) == expected_action
