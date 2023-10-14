import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
@pytest.mark.parametrize(
    "prediction_rate, expected_result",
    [
        [105.1, "Buy more cryptocurrency"],
        [94, "Sell all your cryptocurrency"],
        [105, "Do nothing"],
        [95, "Do nothing"],
        [102, "Do nothing"]
    ])
def test_cryptocurrency_action(
    mock_prediction: callable,
    prediction_rate: int | float,
    expected_result: str
) -> None:
    mock_prediction.return_value = prediction_rate
    result = cryptocurrency_action(100)
    assert result == expected_result
