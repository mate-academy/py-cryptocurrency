from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: int) -> None:
    mock_prediction.return_value = 110  # > 5% increase from 100
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: int) -> None:
    mock_prediction.return_value = 90  # > 5% decrease from 100
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_small_increase(mock_prediction: int) -> None:
    mock_prediction.return_value = 104.9  # < 5% increase from 100
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_small_decrease(mock_prediction: int) -> None:
    mock_prediction.return_value = 95.1  # > 95% of 100
    assert cryptocurrency_action(100) == "Do nothing"
