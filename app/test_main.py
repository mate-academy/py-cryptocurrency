from _pytest.monkeypatch import MonkeyPatch
import app.main as m


def test_buy_more(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(m, "get_exchange_rate_prediction", lambda x: x * 1.06)
    assert m.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(m, "get_exchange_rate_prediction", lambda x: x * 0.94)
    assert m.cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_middle(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(m, "get_exchange_rate_prediction", lambda x: x * 1.02)
    assert m.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_exact_upper_boundary(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(m, "get_exchange_rate_prediction", lambda x: x * 1.05)
    assert m.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_exact_lower_boundary(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(m, "get_exchange_rate_prediction", lambda x: x * 0.95)
    assert m.cryptocurrency_action(100) == "Do nothing"
