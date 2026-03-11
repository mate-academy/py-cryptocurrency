import pytest
from app.main import cryptocurrency_action


def test_buy_more_when_prediction_is_higher(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.10,
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_when_prediction_is_lower(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 0.90,
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_is_close(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.02,
    )
    assert cryptocurrency_action(100) == "Do nothing"

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 0.98,
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_when_prediction_is_exactly_5_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.05,
    )
    assert cryptocurrency_action(100) == "Do nothing"

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 0.95,
    )
    assert cryptocurrency_action(100) == "Do nothing"
