
from app.main import cryptocurrency_action


def test_cryptocurrency_buy_more(monkeypatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda *args: 1100)
    assert cryptocurrency_action(1000) == "Buy more cryptocurrency"


def test_cryptocurrency_sell_all(monkeypatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda *args: 80)
    assert cryptocurrency_action(90) == "Sell all your cryptocurrency"


def test_cryptocurrency_do_nothing(monkeypatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda *args: 102)
    assert cryptocurrency_action(100) == "Do nothing"
