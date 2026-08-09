import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,predicted_rate,result",
    [
        (100, 106, "Buy more cryptocurrency"),
        (200, 210, "Do nothing"),
        (50, 50, "Do nothing"),
        (300, 285, "Do nothing"),
        (300, 284, "Sell all your cryptocurrency")
    ]
)
def test_buy(current_rate: int, predicted_rate: int, result: str) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as predict:
        predict.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == result
