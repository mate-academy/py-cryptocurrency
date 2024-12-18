from _pytest.monkeypatch import MonkeyPatch
from app.main import cryptocurrency_action


def test_buy_cryptocurrency_action(monkeypatch: MonkeyPatch) -> None:
    rate = 1
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda predicted_rate: predicted_rate * 1.06
    )
    assert cryptocurrency_action(rate) == "Buy more cryptocurrency"


def test_sell_cryptocurrency_action(monkeypatch: MonkeyPatch) -> None:
    rate = 1
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda predicted_rate: predicted_rate * 0.94
    )
    assert cryptocurrency_action(rate) == "Sell all your cryptocurrency"


def test_do_nothing_cryptocurrency_action(monkeypatch: MonkeyPatch) -> None:
    rate = 1
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda predicted_rate: predicted_rate * 0.95
    )
    assert cryptocurrency_action(rate) == "Do nothing"

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda predicted_rate: predicted_rate * 1.05
    )
    assert cryptocurrency_action(rate) == "Do nothing"
