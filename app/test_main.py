from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency_when_rate_is_more_than_5_percent_higher(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 106.0
    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency_when_rate_is_more_than_5_percent_lower(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 94.0
    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_exactly_5_percent_higher(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 105.0
    assert cryptocurrency_action(100.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_exactly_5_percent_lower(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 95.0
    assert cryptocurrency_action(100.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_unchanged(
    mock_get_exchange_rate_prediction: MagicMock,
) -> None:
    mock_get_exchange_rate_prediction.return_value = 100.0
    assert cryptocurrency_action(100.0) == "Do nothing"
