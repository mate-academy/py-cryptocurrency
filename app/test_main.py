import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "exchange_rate_prediction, current_rate, expected_result",
    [
        (8, 7.5, "Buy more cryptocurrency"),
        (8, 8.5, "Sell all your cryptocurrency"),
        (21, 20, "Do nothing"),
        (19, 20, "Do nothing")
    ]
)
def test_predict_cryptocurrency_action(
        exchange_rate_prediction: int,
        current_rate: float,
        expected_result: str
) -> None:
    with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=exchange_rate_prediction
    ):
        result = cryptocurrency_action(current_rate)
        assert result == expected_result
