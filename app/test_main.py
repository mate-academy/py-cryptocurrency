import pytest
from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,result", [
        (250, "Buy more cryptocurrency"),
        (81, "Sell all your cryptocurrency"),
        (100, "Do nothing"),
        (95, "Do nothing"),
        (105, "Do nothing"),
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction(
        mock_get_exchange_rate_prediction: MagicMock,
        prediction_rate: int,
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(100) == result
