from unittest import mock
from app.main import cryptocurrency_action
import pytest


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (1.01, 1.02, "Do nothing"),
        (1, 1.05, "Buy more cryptocurrency"),
        (1, 0.95, "Sell all your cryptocurrency"),
        (1.03, 1.11, "Buy more cryptocurrency"),
        (1.3, 0.94, "Sell all your cryptocurrency")
    ]
)
def test_get_exchange_rate_prediction(
        current_rate: float,
        prediction_rate: float,
        result: str
) -> None:
    with mock.patch("app.main.get_exchange_rate_prediction") as mocked_rate:
        mocked_rate.return_value = prediction_rate
        assert cryptocurrency_action(current_rate) == result
