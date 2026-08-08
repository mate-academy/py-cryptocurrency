from unittest import mock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more(monkeypatch):
    monkeypatch.return_value = 10
    assert cryptocurrency_action(8) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all(monkeypatch):
    monkeypatch.return_value = 10
    assert cryptocurrency_action(12) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing(monkeypatch):
    monkeypatch.return_value = 10
    assert cryptocurrency_action(10) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_bound_down(monkeypatch):
    monkeypatch.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_bound_up(monkeypatch):
    monkeypatch.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"
