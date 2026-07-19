from app.main import cryptocurrency_action
from app import main
from _pytest.monkeypatch import MonkeyPatch


def test_cryptocurrency_if_prediction_rate_positive(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 106)
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_if_prediction_rate_negative(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 94)
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_if_prediction_rate_neutral(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 100)
    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_if_prediction_rate_105(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 105)
    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_if_prediction_rate_95(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 95)
    assert cryptocurrency_action(100) == "Do nothing"
