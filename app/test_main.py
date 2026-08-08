from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_rate_grows_more_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 1.06
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_when_rate_drops_more_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 0.94
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_stable(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 1.0
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exactly_5_percent_higher(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 1.05
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_at_exactly_5_percent_lower(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 0.95
    assert cryptocurrency_action(1.0) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_just_above_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 1.051
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_just_below_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 0.949
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"
