import pytest
from unittest import mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, exchange_rate, prediction_message",
    [pytest.param(100, 105, "Do nothing",
                  id="if increase rate less than 5% should do nothing"),
     pytest.param(100, 95, "Do nothing",
                  id="if decrease rate less than 5% should do nothing"),
     pytest.param(100, 150, "Buy more cryptocurrency",
                  id="should to buy coin"),
     pytest.param(100, 60, "Sell all your cryptocurrency",
                  id="should to sell coin")])
@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(
        mock_get_exchange_rate_prediction,
        current_rate,
        exchange_rate,
        prediction_message
):
    mock_get_exchange_rate_prediction.return_value = exchange_rate

    assert cryptocurrency_action(current_rate) == prediction_message
