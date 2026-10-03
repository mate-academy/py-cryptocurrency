from pytest import MonkeyPatch

from app.main import cryptocurrency_action


def test_exchange_rate_110_buy(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 1.10
    )

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_exchange_rate_90_sell(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 0.9
    )

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_exchange_rate_95_do_nothing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 0.95
    )

    assert cryptocurrency_action(1) == "Do nothing"


def test_exchange_rate_105_do_nothing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 1.05
    )

    assert cryptocurrency_action(1) == "Do nothing"
