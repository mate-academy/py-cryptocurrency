from app.main import cryptocurrency_action
from _pytest.monkeypatch import MonkeyPatch


def test_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.10
    )
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 0.90
    )
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


def test_do_nothing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 1.05
    )
    result = cryptocurrency_action(100)
    assert result == "Do nothing"

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: rate * 0.95
    )
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
