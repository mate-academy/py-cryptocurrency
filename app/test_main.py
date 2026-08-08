from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected_result",
    [
        (1, 1.06, "Buy more cryptocurrency"),
        (1, 0.94, "Sell all your cryptocurrency"),
        (1, 0.95, "Do nothing"),
        (1, 1.05, "Do nothing")
    ],
    ids=[
        "Return 'Buy more cryptocurrency' if prediction_rate == 1.06",
        "Return 'Sell all your cryptocurrency' if prediction_rate == 0.94",
        "Return 'Do nothing' if prediction_rate == 0.95",
        "Return 'Do nothing' if prediction_rate == 1.05",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction_rate: mock,
        current_rate: int,
        prediction_rate: float,
        expected_result: str
) -> None:
    mocked_prediction_rate.return_value = prediction_rate

    assert cryptocurrency_action(current_rate) == expected_result
