import pytest
from app.main import cryptocurrency_action


def test_buy_more(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 106
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 94
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_increase(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 104
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_decrease(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 96
    )
    assert cryptocurrency_action(100) == "Do nothing"
