from unittest.mock import patch
from app.main import cryptocurrency_action
from typing import Any


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action(mock_get_exchange_rate_prediction: Any) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1) == "Buy more cryptocurrency", \
        ("Expected 'Buy more cryptocurrency' when prediction_rate is "
         "more than 5% higher than current_rate")

    mock_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency", \
        ("Expected 'Sell all your cryptocurrency' when prediction_rate "
         "is more than 5% lower than current_rate")

    mock_get_exchange_rate_prediction.return_value = 1.02
    assert cryptocurrency_action(1) == "Do nothing", \
        ("Expected 'Do nothing' when prediction_rate "
         "is within 5% of current_rate")

    mock_get_exchange_rate_prediction.return_value = 0.98
    assert cryptocurrency_action(1) == "Do nothing", \
        ("Expected 'Do nothing' when prediction_rate is"
         " within 5% of current_rate")

    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing", \
        ("Expected 'Do nothing' when prediction_rate is exactly 5% higher "
         "than current_rate")

    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing", \
        ("Expected 'Do nothing' when prediction_rate is exactly 5% lower "
         "than current_rate")

    current_rate = 100
    mock_get_exchange_rate_prediction.return_value = 106
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency", \
        ("Expected 'Buy more cryptocurrency' when prediction_rate is 6% higher"
         " than current_rate")

    mock_get_exchange_rate_prediction.return_value = 94
    assert cryptocurrency_action(current_rate) == ("Sell all your "
           "cryptocurrency"), \
        ("Expected 'Sell all your cryptocurrency' when prediction_rate is 6% "
         "lower than current_rate")

    mock_get_exchange_rate_prediction.return_value = 103
    assert cryptocurrency_action(current_rate) == "Do nothing", \
        ("Expected 'Do nothing' when prediction_rate is within 5%"
         " of current_rate")

    mock_get_exchange_rate_prediction.return_value = 97
    assert cryptocurrency_action(current_rate) == "Do nothing", \
        ("Expected 'Do nothing' when prediction_rate is within 5% "
         "of current_rate")
