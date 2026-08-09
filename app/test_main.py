import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predict_curr, curr_result",
    [
        (100, 110, "Buy more cryptocurrency"),
        (100, 90, "Sell all your cryptocurrency"),
        (100 , 105.1, "Buy more cryptocurrency"),
        (100, 94.99, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 105, "Do nothing")
    ]
)
def test_crypto_func(
        current_rate: int | float,
        predict_curr: int | float,
        curr_result: str
) -> None:
    with (
        patch("app.main.get_exchange_rate_prediction") as mock_ex_rate
    ):
        mock_ex_rate.return_value = predict_curr
        result = cryptocurrency_action(current_rate)
        assert result == curr_result
