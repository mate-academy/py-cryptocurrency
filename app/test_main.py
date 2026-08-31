import pytest
from unittest import mock

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,prediction_rate,expected",
    [
        (10.0,
         10.7,
         "Buy more cryptocurrency"),
        (10.0,
         10.5,
         "Do nothing"),
        (10.0,
         9.5,
         "Do nothing"),
        (10.0,
         9.0,
         "Sell all your cryptocurrency"),

    ]
)
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction: float,
        current_rate: float,
        prediction_rate: float,
        expected: str
) -> None:
    mock_get_exchange_rate_prediction.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected
