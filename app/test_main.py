from _pytest.monkeypatch import MonkeyPatch
import app.main


def test_when_predicted_exchange_is_higher(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        app.main, "get_exchange_rate_prediction", lambda current_rate: 48
    )
    result = app.main.cryptocurrency_action(38)
    assert result == "Buy more cryptocurrency"


def test_when_predicted_exchange_is_lower(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        app.main, "get_exchange_rate_prediction", lambda current_rate: 17
    )
    result = app.main.cryptocurrency_action(34)
    assert result == "Sell all your cryptocurrency"


def test_when_difference_is_small(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        app.main, "get_exchange_rate_prediction", lambda current_rate: 10
    )
    result = app.main.cryptocurrency_action(10)
    assert result == "Do nothing"


def test_95_percent_do_nothing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        app.main, "get_exchange_rate_prediction", lambda current_rate: 20.9
    )
    result = app.main.cryptocurrency_action(22)
    assert result == "Do nothing"


def test_105_percent_do_nothing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        app.main, "get_exchange_rate_prediction", lambda current_rate: 8.4
    )
    result = app.main.cryptocurrency_action(8)
    assert result == "Do nothing"
