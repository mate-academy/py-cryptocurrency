import pytest
from unittest.mock import patch
from app import main


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected",
    [
        (100, 106, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 95, "Do nothing"),
        (100, 94, "Sell all your cryptocurrency")
    ],
)
def test_buy_more_cryptocurrency(current_rate: int,
                                 prediction_rate: int,
                                 expected: str) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = prediction_rate
        assert main.cryptocurrency_action(current_rate) == expected
        mock_prediction.assert_called_once_with(current_rate)
