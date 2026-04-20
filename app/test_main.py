from pytest import MonkeyPatch

from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 106
    )

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 94
    )

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_when_rate_is_the_same(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 100
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_when_rate_is_5_percent_higher(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 105
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_when_rate_is_5_percent_lower(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 95
    )

    assert cryptocurrency_action(100) == "Do nothing"
