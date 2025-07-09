from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: patch) -> None:
    mock_prediction.return_value = 1.06  # +6% от 1.0
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: patch) -> None:
    mock_prediction.return_value = 0.94  # −6% от 1.0
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_upper_boundary(mock_prediction: patch) -> None:
    mock_prediction.return_value = 1.05  # ровно +5%
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lower_boundary(mock_prediction: patch) -> None:
    mock_prediction.return_value = 0.95  # ровно −5%
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_small_change(mock_prediction: patch) -> None:
    mock_prediction.return_value = 1.02  # +2%
    assert cryptocurrency_action(1.0) == "Do nothing"
