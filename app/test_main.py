from unittest.mock import patch
import pytest
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predict_rate,result",
    [
        (100, 90, "Sell all your cryptocurrency"),
        (100, 120, "Buy more cryptocurrency"),
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing")
    ]
)
def test_crypto_action(current_rate: int | float,
                       predict_rate: int | float,
                       result: str) -> None:
    with patch("app.main.get_exchange_rate_prediction",
               return_value=predict_rate):
        assert cryptocurrency_action(current_rate) == result
