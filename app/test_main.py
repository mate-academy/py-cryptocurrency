import pytest

from app import main
from app.main import cryptocurrency_action


def test_buy_when_rate_increases_more_than_5_percent(
        monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda rate: 106
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_when_rate_decreases_more_than_5_percent(
        monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda rate: 94
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_when_rate_does_not_change(
        monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda rate: 100
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_on_exact_upper_boundary(
        monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda rate: 105
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_on_exact_lower_boundary(
        monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda rate: 95
    )
    assert cryptocurrency_action(100) == "Do nothing"
