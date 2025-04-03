import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction,result",
    [
        (100, 94, "Sell all your cryptocurrency"),
        (100, 95, "Do nothing"),
        (100, 100, "Do nothing"),
        (100, 105, "Do nothing"),
        (100, 106, "Buy more cryptocurrency"),
        (100.1, 95.094, "Sell all your cryptocurrency"),
        (100.1, 95.095, "Do nothing"),
        (100.1, 100.00, "Do nothing"),
        (100.1, 105.105, "Do nothing"),
        (100.1, 105.106 , "Buy more cryptocurrency"),
    ]
)
def test_cryptocurrency_action(current_rate: int | float,
                               prediction: int | float,
                               result: str
                               ) -> None:
    with (mock.patch("app.main.get_exchange_rate_prediction")
          as get_exchange_rate_prediction):
        get_exchange_rate_prediction.return_value = prediction
        assert cryptocurrency_action(current_rate) == result
