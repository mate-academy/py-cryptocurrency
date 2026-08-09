from typing import Any
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda x: 120.0
    )

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda x: 80.0
    )

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda x: 100.0
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_105_percent_do_nothing(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda x: 105.0
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_95_percent_do_nothing(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda x: 95.0
    )
    assert cryptocurrency_action(100) == "Do nothing"
