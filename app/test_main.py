from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction", return_value=105)
def test_do_nothing_when_rate_is_exactly_5_percent_above(
    mock_exchange_rate: MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=106)
def test_return_buy_more_if_rate_more_then_5_percent(
    mock_exchange_rate: MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction", return_value=100)
def test_do_nothing_when_rate_in_range_5_percents(
    mock_exchange_rate: MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=95)
def test_do_nothing_when_rate_its_5_percent_to_down(
    mock_exchange_rate: MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction", return_value=94)
def test_return_sell_all_when_rate_below_then_5_percents(
    mock_exchange_rate: MagicMock
) -> None:
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"
