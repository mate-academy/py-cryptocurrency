import pytest
from app.main import cryptocurrency_action


def test_buy_more(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_rate(rate: float) -> float:
        return rate * 1.06

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", fake_rate
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_rate(rate: float) -> float:
        return rate * 0.94

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", fake_rate
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_upper(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_rate(rate: float) -> float:
        return rate * 1.05

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", fake_rate
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_lower(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_rate(rate: float) -> float:
        return rate * 0.95

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", fake_rate
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_no_change(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_rate(rate: float) -> float:
        return rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", fake_rate
    )
    assert cryptocurrency_action(100) == "Do nothing"
