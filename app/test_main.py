import pytest
from unittest.mock import patch
from unittest.mock import Mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,result",
    [
        (150, 100, "Buy more cryptocurrency"),
        (40, 50, "Sell all your cryptocurrency"),
        (205, 200, "Do nothing"),
        (210, 200, "Do nothing"),
        (190, 200, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_prediction(
        mock_get_exchange: Mock,
        current_rate: int | float,
        prediction_rate: int | float,
        result: str
) -> None:
    mock_get_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
