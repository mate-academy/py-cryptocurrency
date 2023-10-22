from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_rate",
    [
        (0.8, 1, "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (1.5, 1, "Buy more cryptocurrency"),
        (0.95, 1, "Do nothing"),
        (1.03, 1, "Do nothing"),
        (1.05, 1, "Do nothing")

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock,
        prediction_rate: float,
        current_rate: float,
        expected_rate: str
) -> None:

    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_rate
