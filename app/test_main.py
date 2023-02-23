from pytest import MonkeyPatch

from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 11.7
    )
    assert cryptocurrency_action(9.8) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 7
    )
    assert cryptocurrency_action(8) == "Sell all your cryptocurrency"


def test_do_nothing_up_5(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 95
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_down_5(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 105
    )
    assert cryptocurrency_action(100) == "Do nothing"
