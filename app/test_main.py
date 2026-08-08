from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_when_prediction_is_high(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_cryptocurrency_when_prediction_is_low(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_is_exactly_five_percent_higher(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_is_exactly_five_percent_lower(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_prediction_is_insignificantly_different(
    mock_prediction: MagicMock
) -> None:
    # Prediction is within the 5% range
    mock_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
