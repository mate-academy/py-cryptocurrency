from typing import Callable
from app.main import cryptocurrency_action


def test_cryptocurrency_buy_more(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda *args: 1100)
    assert cryptocurrency_action(1000) == "Buy more cryptocurrency"


def test_cryptocurrency_sell_all(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda *args: 80)
    assert cryptocurrency_action(90) == "Sell all your cryptocurrency"


def test_cryptocurrency_do_nothing(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda *args: 102)
    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_95(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda *args: 95)
    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_1_05(monkeypatch: Callable) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda *args: 105)
    assert cryptocurrency_action(100) == "Do nothing"
