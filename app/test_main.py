import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (100, 105, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (200, 200, "Do nothing"),
        (40, 50, "Buy more cryptocurrency"),
        (50, 49, "Do nothing"),
        (50, 47, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        current_rate: int,
        prediction_rate: int,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as prediction:
        prediction.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
