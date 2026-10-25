
from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_when_rate_increases_more_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_when_rate_decreases_more_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_increases_less_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 104
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_decreases_less_than_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 96
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_increases_exactly_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_decreases_exactly_5_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"
