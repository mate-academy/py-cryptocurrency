import pytest

from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (1, 0.95, "Buy more cryptocurrency"),
        (1, 1.06, "Sell all your cryptocurrency"),
        (1, 0.99, "Do nothing"),
        (1.05, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (0, 1, "Sell all your cryptocurrency"),
        (1000000, 0.000001, "Buy more cryptocurrency")
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: mock.Mock,
        prediction_rate: int | float,
        current_rate: int | float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
