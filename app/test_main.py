from unittest.mock import patch
from .main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_buy_more(mocked_rate: int) -> None:
    mocked_rate.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_sell_all(mocked_rate: int) -> None:
    mocked_rate.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_do_nothing(mocked_rate: int) -> None:
    mocked_rate.return_value = 100
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_exactly_5_percent_up(mocked_rate: int) -> None:
    mocked_rate.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_action_exactly_5_percent_down(
        mocked_rate: int) -> None:
    mocked_rate.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
