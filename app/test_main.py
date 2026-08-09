# flake8: noqa: *
from unittest import mock
import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "prediction_rate,current_rate,expected",
    [
        pytest.param(106, 100, "Buy more cryptocurrency", id="Predicted rate more than 5%"),
        pytest.param(94, 100, "Sell all your cryptocurrency", id="Predicted rate less than 5%"),
        pytest.param(101, 100, "Do nothing", id="Predicted rate doesn't more or less than 5%"),
        pytest.param(105, 100, "Do nothing", id="Predicted rate more == 5%"),
        pytest.param(95, 100, "Do nothing", id="Predicted rate less == 5%"),
    ]
)
@mock.patch('app.main.get_exchange_rate_prediction')
def test_logic(mock_exchange, prediction_rate, current_rate, expected):
    mock_exchange.return_value = prediction_rate
    assert cryptocurrency_action(current_rate) == expected


