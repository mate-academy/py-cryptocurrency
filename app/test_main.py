from app.main import cryptocurrency_action
from unittest.mock import patch, Mock


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction: Mock)\
        -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction: Mock)\
        -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction: Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing", \
        ("You should not sell cryptocurrency when prediction_rate "
         "/ current_rate == 0.95")

    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing", \
        ("You should not buy cryptocurrency when prediction_rate "
         "/ current_rate == 1.05")

    mock_get_exchange_rate_prediction.return_value = 0.951
    assert cryptocurrency_action(1.0) == "Do nothing", \
        "You should not sell cryptocurrency within ±5% range"

    mock_get_exchange_rate_prediction.return_value = 1.049
    assert cryptocurrency_action(1.0) == "Do nothing", \
        "You should not buy cryptocurrency within ±5% range"
