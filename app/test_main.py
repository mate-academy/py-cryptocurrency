from app.main import cryptocurrency_action
from unittest.mock import patch, MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_if_rate_increases_over_5_percent(
    mock_predict: MagicMock
) -> None:
    current_rate = 100
    mock_predict.return_value = 105.01
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_if_rate_drops_over_5_percent(
    mock_predict: MagicMock
) -> None:
    current_rate = 100
    mock_predict.return_value = 94.99
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_if_rate_change_is_within_5_percent(
    mock_predict: MagicMock
) -> None:
    current_rate = 100
    mock_predict.return_value = 102
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_increase_is_exactly_5_percent(
    mock_predict: MagicMock
) -> None:
    current_rate = 100
    mock_predict.return_value = 105.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_decrease_is_exactly_5_percent(
    mock_predict: MagicMock
) -> None:
    current_rate = 100
    mock_predict.return_value = 95.0
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
