from unittest.mock import patch
import pytest
from typing import Callable
from main import cryptocurrency_action


@patch("main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 110
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 85
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("main.get_exchange_rate_prediction")
def test_do_nothing(
    mock_get_exchange_rate_prediction: Callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


if __name__ == "__main__":
    pytest.main()
