from app.main import cryptocurrency_action
from unittest.mock import patch, MagicMock


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_predicted_rate_higher(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_when_predicted_rate_lower(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_almost_same(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 103
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_exactly_5_percent_higher(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_exactly_5_percent_lower(
    mock_prediction: MagicMock
) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
