from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_func_returns_correct_values(
    mocked_func: MagicMock
) -> None:
    mocked_func.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_func_returns_correct_values1(
    mocked_func: MagicMock
) -> None:
    mocked_func.return_value = 105.001
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_func_returns_correct_values2(
    mocked_func: MagicMock
) -> None:
    mocked_func.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_func_returns_correct_values3(
    mocked_func: MagicMock
) -> None:
    mocked_func.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
