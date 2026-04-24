from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_when_prediction_more_than_5_percent(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_when_prediction_less_than_5_percent(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_5_higher_percent(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_5_lower_percent(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_difference_small(
        mock_get_exchange_rate_prediction: int
) -> None:
    mock_get_exchange_rate_prediction.return_value = 102
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
