from unittest.mock import patch
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_crypto(mock_prediction: int) -> None:
    mock_prediction.return_value = 110

    result = cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_crypto(mock_prediction: int) -> None:
    mock_prediction.return_value = 90

    result = cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_if_difference_is_less_than_5_percent(
        mock_prediction: int) -> None:
    mock_prediction.return_value = 104

    result = cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_on_upper_boundary(mock_prediction: int) -> None:
    mock_prediction.return_value = 105

    result = cryptocurrency_action(100)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_on_lower_boundary(mock_prediction: int) -> None:
    mock_prediction.return_value = 95

    result = cryptocurrency_action(100)

    assert result == "Do nothing"
