import pytest

from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "curr_rate, prediction_rate, expected_res",
    [
        (1, 1, "Do nothing"),
        (2, 1.5, "Sell all your cryptocurrency"),
        (1.1, 2, "Buy more cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ]
)
def test_get_exchange_rate_prediction(
    curr_rate: int | float,
    prediction_rate: int | float,
    expected_res: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_predict:
        mocked_predict.return_value = prediction_rate
        assert cryptocurrency_action(curr_rate) == expected_res
