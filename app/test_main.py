from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_when_prediction_is_higher_than_five_percent(
    mock_prediction: Mock
) -> None:
    mock_prediction.return_value = 106.0
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_when_prediction_is_lower_than_five_percent(
    mock_prediction: Mock
) -> None:
    mock_prediction.return_value = 94.0
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_difference_is_small(
    mock_prediction: Mock
) -> None:
    mock_prediction.return_value = 102.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_is_exactly_five_percent_higher(
    mock_prediction: Mock
) -> None:
    mock_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_is_exactly_five_percent_lower(
    mock_prediction: Mock
) -> None:
    mock_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"
