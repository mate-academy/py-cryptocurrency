from app.main import cryptocurrency_action
from pytest import MonkeyPatch


def test_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda current_rate: 106)
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def sell_all_your_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda current_rate: 94)
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_upper_border(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda current_rate: 105)
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_lower_border(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda current_rate: 95)
    assert cryptocurrency_action(100) == "Do nothing"
