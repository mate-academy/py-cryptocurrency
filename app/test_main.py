import app.main
from app.main import cryptocurrency_action
from typing import Any


def test_buy_more(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda current: current * 1.10,
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda current: current * 0.90,
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_between_thresholds(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda current: current * 1.03,
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_105_percent_should_do_nothing(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda current: current * 105 / 100,
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_95_percent_should_do_nothing(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda current: current * 95 / 100,
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_just_above_and_below_thresholds(monkeypatch: Any) -> None:
    eps = 1e-6

    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda current: current * (1.05 + eps),
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"

    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda current: current * (0.95 - eps),
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
