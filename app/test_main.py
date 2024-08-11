from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("main.get_exchange_rate_prediction")
def test_do_nothing(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 102
    assert cryptocurrency_action(100) == "Do nothing"


@patch("main.get_exchange_rate_prediction")
def test_do_nothing_close_to_threshold(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 104.9
    assert cryptocurrency_action(100) == "Do nothing"

    mock_get_exchange_rate_prediction.return_value = 95.1
    assert cryptocurrency_action(100) == "Do nothing"
