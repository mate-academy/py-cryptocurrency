from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.1)
def test_prediction_buy(mock_get_exchange_rate_prediction: float) -> None:
    assert cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.9)
def test_prediction_sell(mock_get_exchange_rate_prediction: float) -> None:
    assert cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=1.05)
def test_rate_105_percent_do_nothing(
        mock_get_exchange_rate_prediction: float
) -> None:
    assert cryptocurrency_action(1.0) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction", return_value=0.95)
def test_rate_095_percent_do_nothing(
        mock_get_exchange_rate_prediction: float) -> None:
    assert cryptocurrency_action(1.0) == "Do nothing"
