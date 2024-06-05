from typing import Any

import app.main


def test_buy_more_cryptocurrency_action(monkeypatch: Any) -> None:
    current_rate = 100
    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", lambda x: 106)
    assert app.main.cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_sell_cryptocurrency_action(monkeypatch: Any) -> None:
    current_rate = 100
    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", lambda x: 94)
    assert app.main.cryptocurrency_action(current_rate) == "Sell all your cryptocurrency"


def test_do_nothing_cryptocurrency_action1(monkeypatch: Any) -> None:
    current_rate = 100
    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", lambda x: 103)
    assert app.main.cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_cryptocurrency_action2(monkeypatch: Any) -> None:
    current_rate = 100
    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", lambda x: 105)
    assert app.main.cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_cryptocurrency_action3(monkeypatch: Any) -> None:
    current_rate = 100
    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", lambda x: 95)
    assert app.main.cryptocurrency_action(current_rate) == "Do nothing"
