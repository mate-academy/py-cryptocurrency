from app.main import cryptocurrency_action
from pytest import MonkeyPatch


def test_correct_prediction_buy(monkeypatch: MonkeyPatch) -> None:

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 1.06
    )
    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_correct_prediction_sell(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 0.94
    )
    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_correct_prediction_equal(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 1.04
    )
    assert cryptocurrency_action(1) == "Do nothing"


def test_correct_prediction_equal_2(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda rate: 0.96
    )
    assert cryptocurrency_action(1) == "Do nothing"
