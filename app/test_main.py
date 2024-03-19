from unittest.mock import patch, MagicMock

import pytest

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_was_called_with(
        mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 1.1
    cryptocurrency_action(1)
    mock_prediction.assert_called_once_with(1)


@pytest.mark.parametrize(
    "return_rate,expected_result",
    [
        (1.06, "Buy more cryptocurrency"),
        (1.05, "Do nothing"),
        (0.9499, "Sell all your cryptocurrency"),
        (0.95, "Do nothing")
    ],
    ids=[
        "Predicted exchange rate is more than 5% higher from the current",
        "Difference is not that much",
        "Predicted exchange rate is more than 5% lower from the current",
        "Difference is not that much"
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_should_return_expected_result(
        mock_prediction: MagicMock,
        return_rate: float,
        expected_result: str
) -> None:
    mock_prediction.return_value = return_rate
    assert cryptocurrency_action(1) == expected_result
