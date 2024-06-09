# import pytest
from app.main import cryptocurrency_action
from unittest.mock import patch


def test_buy_more_cryptocurrency() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.06 * 100
        action = cryptocurrency_action(100)
        assert action == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 0.94 * 100
        action = cryptocurrency_action(100)
        assert action == "Sell all your cryptocurrency"


def test_do_nothing() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.03 * 100
        action = cryptocurrency_action(100)
        assert action == "Do nothing"


def test_buy_more_edge_case() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.05 * 100
        action = cryptocurrency_action(100)
        assert action == "Do nothing"


def test_sell_all_edge_case() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 0.95 * 100
        action = cryptocurrency_action(100)
        assert action == "Do nothing"


def test_do_nothing_edge_case() -> None:
    with (patch("app.main.get_exchange_rate_prediction")
          as mock_get_exchange_rate_prediction):
        mock_get_exchange_rate_prediction.return_value = 1.00 * 100
        action = cryptocurrency_action(100)
        assert action == "Do nothing"
