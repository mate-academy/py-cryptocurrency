import pytest
from app import main


def test_should_buy(monkeypatch):
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda _: 110.0)
    assert main.cryptocurrency_action(100.0) == "Buy more cryptocurrency"


def test_should_sell(monkeypatch):
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda _: 90.0)
    assert main.cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


def test_should_do_nothing_when_close_to_rate(monkeypatch):
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda _: 97.0)
    assert main.cryptocurrency_action(100.0) == "Do nothing"


def test_should_do_nothing_when_exactly_same(monkeypatch):
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda _: 100.0)
    assert main.cryptocurrency_action(100.0) == "Do nothing"
