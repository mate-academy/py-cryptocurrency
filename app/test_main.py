import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,result",
    [
        (10, 18, "Buy more cryptocurrency"),
        (20, 10, "Sell all your cryptocurrency"),
        (30, 29, "Do nothing"),
        (30, 31, "Do nothing"),
        (30, 30.9, "Do nothing")
    ],
    ids=[
        "buy if predicted exchange rate `5%` higher",
        "sell if predicted exchange rate `5%` lower",
        "do nothing if difference is not that much",
        "do nothing if difference is not that much",
        "do nothing if difference is not that much"
    ]
)
def test_cryptocurrency_action(
    current_rate: int | float,
    predicted_rate: int | float,
    result: str
) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as mock_exchange_rate_prediction):
        mock_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == result
