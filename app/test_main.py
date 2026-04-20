from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 106
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 94
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_equal(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_upper_boundary(mock_prediction: MagicMock) -> None:
    # exactly 5% higher — not MORE than 5%
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lower_boundary(mock_prediction: MagicMock) -> None:
    # exactly 5% lower — not MORE than 5%
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_buy_just_above_boundary(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 105.01
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_just_below_boundary(mock_prediction: MagicMock) -> None:
    mock_prediction.return_value = 94.99
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
