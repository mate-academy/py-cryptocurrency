from __future__ import annotations

from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_buy_action(mocked_prediction: None) -> None:
    mocked_prediction.return_value = 1.5
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_sell_action(mocked_prediction: None) -> None:
    mocked_prediction.return_value = 0.9
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_cryptocurrency_do_nothing_action(mocked_prediction: None) -> None:
    mocked_prediction.return_value = 1.01
    assert cryptocurrency_action(1) == "Do nothing"
