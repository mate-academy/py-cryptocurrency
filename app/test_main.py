import pytest
from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,result",
    [
        (100, 105, "Do nothing"),
        (100, 95, "Do nothing"),
        (200, 210, "Do nothing"),
        (200, 190, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100, 165, "Buy more cryptocurrency"),
        (100, 94, "Sell all your cryptocurrency"),
        (100, 55, "Sell all your cryptocurrency"),
        (200, 211, "Buy more cryptocurrency"),
        (200, 260, "Buy more cryptocurrency"),
        (200, 189, "Sell all your cryptocurrency"),
        (200, 140, "Sell all your cryptocurrency"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        exchange_rate_prediction: MagicMock,
        current_rate: int,
        prediction_rate: int,
        result: str
) -> None:
    exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == result
