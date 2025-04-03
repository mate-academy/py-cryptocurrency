from _pytest.monkeypatch import MonkeyPatch
from app.main import cryptocurrency_action


def test_return_check(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 10.6)
    assert cryptocurrency_action(10) == "Buy more cryptocurrency"
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 10.0)
    assert cryptocurrency_action(10) == "Do nothing"
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 9.2)
    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 10.5)
    assert cryptocurrency_action(10) == "Do nothing"
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda x: 9.5)
    assert cryptocurrency_action(10) == "Do nothing"
