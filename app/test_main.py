from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "rate_prediction,expected_cryptocurrency_action",
    [
        (105, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
        (106, "Buy more cryptocurrency"),
    ],
    ids=[
        "Should do nothing if prediction rate not over 5% from current",
        "Should do nothing if prediction rate not under 5% from current",
        "Should buy more cryptocurrency "
        "if prediction rate higher than 5% from current",
        "Should sell all cryptocurrency "
        "if prediction rate lesser than 5% from current",
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_work_correctly(
        mocked_rate_prediction: mock.Mock,
        rate_prediction: int | float,
        expected_cryptocurrency_action: str
) -> None:
    mocked_rate_prediction.return_value = rate_prediction
    assert cryptocurrency_action(100) == expected_cryptocurrency_action
