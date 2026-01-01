from unittest import mock

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_exchange,prediction_rate,result",
    [
        (100, 106.0, "Buy more cryptocurrency"),
        (100, 94.0, "Sell all your cryptocurrency"),
        (100, 95.0, "Do nothing"),
        (100, 105.0, "Do nothing"),
    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_return_prediction(
        mock_prediction_rate: float,
        current_exchange: int | float,
        prediction_rate: float,
        result: str
) -> None:
    mock_prediction_rate.return_value = prediction_rate
    assert cryptocurrency_action(current_exchange) == result
