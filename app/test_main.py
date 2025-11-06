import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction):
    """Проверка: курс вырастет больше чем на 5% — нужно покупать."""
    current_rate = 100
    mock_prediction.return_value = 110
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction):
    """Проверка: курс упадет больше чем на 5% — нужно продать всё."""
    current_rate = 100
    mock_prediction.return_value = 90
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_small_increase(mock_prediction):
    """Проверка: рост меньше 5% — ничего не делаем."""
    current_rate = 100
    mock_prediction.return_value = 104.9
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_with_small_decrease(mock_prediction):
    """Проверка: падение меньше 5% — ничего не делаем."""
    current_rate = 100
    mock_prediction.return_value = 95.1
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_exactly_five_percent_up(mock_prediction):
    """Проверка: ровно +5% — всё ещё ничего не делаем."""
    current_rate = 100
    mock_prediction.return_value = 105
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_exactly_five_percent_down(mock_prediction):
    """Проверка: ровно -5% — всё ещё ничего не делаем."""
    current_rate = 100
    mock_prediction.return_value = 95
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
