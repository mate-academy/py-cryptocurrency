from unittest.mock import patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_rate_105_percent_do_nothing(
    mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05
    current_rate: float = 1.00
    assert cryptocurrency_action(current_rate) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_95_percent_do_nothing(
    mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95
    current_rate: float = 1.00
    assert cryptocurrency_action(current_rate) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_106_percent_buy_more(
    mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.06
    current_rate: float = 1.00
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_rate_94_percent_sell_all(
    mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94
    current_rate: float = 1.00
    assert (
        cryptocurrency_action(current_rate)
        == "Sell all your cryptocurrency"
    )


@patch("app.main.get_exchange_rate_prediction")
def test_rate_equal_current_rate_do_nothing(
    mock_get_exchange_rate_prediction: callable
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.00
    current_rate: float = 1.00
    assert cryptocurrency_action(current_rate) == "Do nothing"
