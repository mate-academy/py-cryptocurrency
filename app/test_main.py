import pytest
from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate, current_rate, expected_result",
    [
        (1.06, 1.00, "Buy more cryptocurrency"),
        (1.00, 1.06, "Sell all your cryptocurrency"),
        (1.05, 1.00, "Do nothing"),
        (0.95, 1.00, "Do nothing"),
        (1.01, 1.00, "Do nothing"),
    ])
def test_what_to_do_with_crypto(
        mock_get_exchange_rate_prediction: float,
        prediction_rate: int | float,
        current_rate: int | float,

        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    result = cryptocurrency_action(current_rate)
    assert result == expected_result
