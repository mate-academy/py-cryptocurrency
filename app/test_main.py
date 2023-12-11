from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction, expected_result",
    [
        (1.1, "Buy more cryptocurrency"),
        (0.9, "Sell all your cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
        (1, "Do nothing")
    ],
    ids=[
        "Predicted exchange rate is more than 5% higher from the current",
        "Predicted exchange rate is more than 5% lower from the current",
        "Predicted exchange rate is less than 5% change",
        "Predicted exchange rate is 5% higher from the current",
        "Predicted exchange rate is 5% lower from the current"
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_prediction: callable,
        prediction: int | float,
        expected_result: str
) -> None:
    mocked_prediction.return_value = prediction

    assert cryptocurrency_action(1) == expected_result
