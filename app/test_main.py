import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted, expected", [
        pytest.param(
            1.07, "Buy more cryptocurrency",
            id="Should return buy more then predicted increase more than 5%"),
        pytest.param(
            1.13, "Buy more cryptocurrency",
            id="Should return buy more then predicted increase more than 5%"
        ),
        pytest.param(
            0.97, "Do nothing",
            id="Should return do nothing if difference is less than 5%"
        ),
        pytest.param(
            1.0, "Do nothing",
            id="Should return do nothing if difference is less than 5%"
        ),
        pytest.param(
            0.9, "Sell all your cryptocurrency",
            id="Should return sell then predicted decrease more than 5%"
        ),
        pytest.param(
            0.85, "Sell all your cryptocurrency",
            id="Should return sell then predicted decrease more than 5%"
        )
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: patch,
        predicted: float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = predicted
    current_rate = 1.0  # Use a consistent current rate for simplicity
    assert cryptocurrency_action(current_rate) == expected
