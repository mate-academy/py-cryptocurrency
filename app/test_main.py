from unittest import mock
from unittest.mock import Mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_get_exchange_rate_prediction: Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 110
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell(mock_get_exchange_rate_prediction: Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 90
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction: Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 99
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exact_boundaries(mock_get_exchange_rate_prediction: Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_exact_lower_boundary(mock_get_exchange_rate_prediction: Mock) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
