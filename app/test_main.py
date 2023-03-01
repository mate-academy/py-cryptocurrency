import pytest
from app.main import cryptocurrency_action
from unittest import mock


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_output",
    [
        (1.06, 1, "Buy more cryptocurrency"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (0.94, 1, "Sell all your cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mocked_exchange_rate_prediction: mock,
        prediction_rate: float,
        current_rate: int,
        expected_output: str
) -> None:

    mocked_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_output
