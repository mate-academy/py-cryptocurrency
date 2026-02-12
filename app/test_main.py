from pytest import MonkeyPatch

from app import main


def test_should_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * 1.06,
    )

    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_should_sell_all_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * 0.94,
    )

    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_do_nothing_when_prediction_is_exactly_105_percent(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * 1.05,
    )

    assert main.cryptocurrency_action(100) == "Do nothing"


def test_should_do_nothing_when_prediction_is_exactly_95_percent(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * 0.95,
    )

    assert main.cryptocurrency_action(100) == "Do nothing"
