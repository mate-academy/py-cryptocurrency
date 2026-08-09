from unittest.mock import patch, MagicMock
from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 106.0

    result: str = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 94.0

    result: str = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_small_increase(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 104.0

    result: str = cryptocurrency_action(current_rate)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_small_drop(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 96.0

    result: str = cryptocurrency_action(current_rate)

    assert result == "Do nothing"


# ВАЖНЫЕ граничные тесты
@patch("app.main.get_exchange_rate_prediction")
def test_boundary_plus_five_percent(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 105.0

    result: str = cryptocurrency_action(current_rate)

    assert result == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_boundary_minus_five_percent(mock_prediction: MagicMock) -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 95.0

    result: str = cryptocurrency_action(current_rate)

    assert result == "Do nothing"
