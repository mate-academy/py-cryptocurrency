from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_buy_more(
        mock_rate_prediction: callable
) -> None:
    current_rate = 1.00
    mock_rate_prediction.return_value = 1.06
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_sell_all(
        mock_rate_prediction: callable
) -> None:
    current_rate = 1.00
    mock_rate_prediction.return_value = 0.94
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing(
        mock_rate_prediction: callable
) -> None:
    current_rate = 1.00
    mock_rate_prediction.return_value = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
