from unittest.mock import patch
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_the_rate_is_more_than_5_percent_higher(
        mock_get_exchange_rate_prediction: MagicMock) -> None:
    starting_bid = 100
    predictable = 110

    mock_get_exchange_rate_prediction.return_value = predictable

    assert cryptocurrency_action(starting_bid) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_the_rate_is_more_than_5_percent_lower(
        mock_get_exchange_rate_prediction: MagicMock) -> None:
    starting_bid = 100
    predictable = 90

    mock_get_exchange_rate_prediction.return_value = predictable

    assert cryptocurrency_action(starting_bid
                                 ) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_if_the_rate_is_2_percent(
        mock_get_exchange_rate_prediction: MagicMock) -> None:
    starting_bid = 100
    predictable = 102

    mock_get_exchange_rate_prediction.return_value = predictable

    assert cryptocurrency_action(starting_bid
                                 ) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_the_difference_is_not_that_big(
        mock_get_exchange_rate_prediction: MagicMock) -> None:
    starting_bid = 100
    predictable = 105

    mock_get_exchange_rate_prediction.return_value = predictable

    assert cryptocurrency_action(starting_bid) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_the_rate_below(
        mock_get_exchange_rate_prediction: MagicMock) -> None:
    starting_bid = 100
    predictable = 95

    mock_get_exchange_rate_prediction.return_value = predictable

    assert cryptocurrency_action(starting_bid) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_difference_is_not_that_big(
        mock_get_exchange_rate_prediction: MagicMock) -> None:
    starting_bid = 100
    predictable = 101

    mock_get_exchange_rate_prediction.return_value = predictable

    assert cryptocurrency_action(starting_bid) == "Do nothing"
