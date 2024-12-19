import pytest

from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predict_rate, expected",
    [
        (1.5, 1.59, "Buy more cryptocurrency"),
        (1.5, 1.41, "Sell all your cryptocurrency"),
        (1.5, 1.425, "Do nothing"),
        (1.5, 1.5, "Do nothing"),
        (1.5, 1.575, "Do nothing"),
    ],
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: patch,
        current_rate: float,
        predict_rate: float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predict_rate
    response = cryptocurrency_action(current_rate)
    assert response == expected
