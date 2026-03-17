import pytest
from unittest.mock import patch
from app import main


@pytest.mark.parametrize(
    "prediction, action",
    [
        (1.06, "Buy more cryptocurrency"),
        (1.05, "Do nothing"),
        (0.95, "Do nothing"),
        (0.94, "Sell all your cryptocurrency"),
        (1.04, "Do nothing"),
        (0.96, "Do nothing"),
    ],
)
def test_cryptocurrency_action(prediction: float, action: str) -> None:
    with patch("app.main.get_exchange_rate_prediction") as mock_prediction:
        mock_prediction.return_value = prediction

        assert main.cryptocurrency_action(1) == action

        mock_prediction.assert_called_once_with(1)
