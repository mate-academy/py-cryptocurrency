from app.main import cryptocurrency_action
from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
def test_to_buy_more_crypto(mocked_rate: None) -> None:
    mocked_rate.return_value = 1.1

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_to_sell_crypto(mocked_rate: None) -> None:
    mocked_rate.return_value = 0.9

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_to_do_nothing_with_105_procent(mocked_rate: None) -> None:
    mocked_rate.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_to_do_nothing_with_95_procent(mocked_rate: None) -> None:
    mocked_rate.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"
