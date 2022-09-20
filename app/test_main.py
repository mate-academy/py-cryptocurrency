from unittest.mock import patch
from app.main import cryptocurrency_action
import pytest


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_cryptocurrency(mock_rate_prediction):
    mock_rate_prediction.return_value = 1.20
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_cryptocurrency(mock_rate_prediction):
    mock_rate_prediction.return_value = 0.82
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_with_rate_0_95(mock_rate_prediction):
    mock_rate_prediction.return_value = 0.95
    assert cryptocurrency_action(1) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_with_rate_1_05(mock_rate_prediction):
    mock_rate_prediction.return_value = 1.05
    assert cryptocurrency_action(1) == "Do nothing"

