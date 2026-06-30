import pytest
from unittest import mock

import app.main


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        pytest.param(
            15, 15.0, "Do nothing",
            id="test rate did not change",
        ),
        pytest.param(
            100, 105.0, "Do nothing",
            id="test do nothing if rate is no more than 5 percent higher",
        ),
        pytest.param(
            100, 95.0, "Do nothing",
            id="test do nothing if rate is no more than 5 percent lower",
        ),
        pytest.param(
            100, 158.8, "Buy more cryptocurrency",
            id="test rate is more than 5 percent higher",
        ),
        pytest.param(
            100, 65.3, "Sell all your cryptocurrency",
            id="test rate is more than 5 percent lower",
        )
    ]
)
def test_cryptocurrency_action(
    mocked_rate_prediction: mock.MagicMock,
    current_rate: int | float,
    prediction_rate: float,
    expected_result: str
) -> None:
    mocked_rate_prediction.return_value = prediction_rate
    assert app.main.cryptocurrency_action(current_rate) == expected_result
