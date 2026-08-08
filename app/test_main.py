from _pytest.monkeypatch import MonkeyPatch
from app.main import cryptocurrency_action


def test_buy(monkeypatch: MonkeyPatch) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 106.0
    )
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_sell(monkeypatch: MonkeyPatch) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 94.0
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_do_nothing_upper_boundary(monkeypatch: MonkeyPatch) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 105.0
    )
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_lower_boundary(monkeypatch: MonkeyPatch) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 95.0
    )
    assert cryptocurrency_action(current_rate) == "Do nothing"
