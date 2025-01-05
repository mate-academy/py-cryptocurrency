from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: float) -> None:
    current_rate = 100
    mock_prediction.return_value = 106
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: float) -> None:
    current_rate = 100
    mock_prediction.return_value = 94
    assert cryptocurrency_action(
        current_rate
    ) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: float) -> None:
    current_rate = 100
    mock_prediction.return_value = 105
    assert cryptocurrency_action(current_rate) == "Do nothing"
    mock_prediction.return_value = 95
    assert cryptocurrency_action(current_rate) == "Do nothing"
