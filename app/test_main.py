from unittest.mock import patch, MagicMock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,"
    " prediction_rate,"
    " expected_result",
    [
        (1.0, 1.06, "Buy more cryptocurrency"),
        (1.0, 0.94, "Sell all your cryptocurrency"),
        (1.0, 1.05, "Do nothing"),
        (1.0, 0.95, "Do nothing")
    ])
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: MagicMock,
        current_rate: float,
        prediction_rate: float,
        expected_result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected_result
