from unittest.mock import Mock, patch

from app import main


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_when_prediction_is_more_than_five_percent_higher(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 106

    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_when_prediction_is_more_than_five_percent_lower(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 94

    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_difference_is_not_that_much(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 103

    assert main.cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_is_exactly_five_percent_higher(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105

    assert main.cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_prediction_is_exactly_five_percent_lower(
    mock_get_exchange_rate_prediction: Mock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95

    assert main.cryptocurrency_action(100) == "Do nothing"
