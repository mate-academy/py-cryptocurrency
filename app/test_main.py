from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,expected",
    [
        (106, "Buy more cryptocurrency"),
        (105, "Do nothing"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (94, "Sell all your cryptocurrency"),
    ],
    ids=[
        "more than 5% higher: buy",
        "exactly 5% higher: do nothing",
        "same rate: do nothing",
        "exactly 5% lower: do nothing",
        "more than 5% lower: sell",
    ]
)
def test_action_depends_on_predicted_rate(
        prediction_rate: int,
        expected: str
) -> None:
    with mock.patch(
        "app.main.get_exchange_rate_prediction",
        return_value=prediction_rate
    ) as mocked_prediction:
        assert cryptocurrency_action(100) == expected
    mocked_prediction.assert_called_once_with(100)
