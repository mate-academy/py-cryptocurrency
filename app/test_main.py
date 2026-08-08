from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 106
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 94
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_small_increase(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 103
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_small_decrease(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 97
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_exactly_105(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 105
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_is_exactly_95(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 95
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
