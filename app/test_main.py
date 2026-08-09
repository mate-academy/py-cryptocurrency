import pytest
from typing import Union
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [(10, 10, "Do nothing"),
     (10, 10.6, "Buy more cryptocurrency"),
     (10, 9.4, "Sell all your cryptocurrency"),
     (10, 10.5, "Do nothing"),
     (10, 9.5, "Do nothing")]
)
@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: int | float,
        current_rate: Union[int, float],
        prediction_rate: int | float,
        result: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
