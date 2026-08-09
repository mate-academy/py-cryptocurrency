from unittest.mock import patch
from app.main import cryptocurrency_action
from unittest import mock


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction: mock)\
        -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction: mock) \
        -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction: mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.02
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_exact(mock_get_exchange_rate_prediction: mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_(mock_get_exchange_rate_prediction: mock) \
        -> None:
    mock_get_exchange_rate_prediction.return_value = 1.051
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_difference(mock_get_exchange_rate_prediction: mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.949
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_asf_sell_all_cryptocurrency(mock_get_exchange_rate_prediction: mock) \
        -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"
