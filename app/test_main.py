from app.main import cryptocurrency_action
import pytest


def test_buy_more_cryptocurrency(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.06
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 0.94
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.03
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_boundary_exactly_105_percent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.05
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_boundary_exactly_95_percent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 0.95
    )
    assert cryptocurrency_action(100) == "Do nothing"
