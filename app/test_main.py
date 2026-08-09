import app.main


from typing import Any


from app.main import cryptocurrency_action


def test_return_buy_if_high(monkeypatch: Any) -> None:
    def mock_rate(*args, **kwargs) -> float:
        return 99999999

    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", mock_rate)

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_return_sell_if_low(monkeypatch: Any) -> None:
    def mock_rate(*args, **kwargs) -> float:
        return 1

    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", mock_rate)

    assert cryptocurrency_action(99999999) == "Sell all your cryptocurrency"


def test_do_nothing_if_105(monkeypatch: Any) -> None:
    def mock_rate(*args, **kwargs) -> float:
        return 1.05

    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", mock_rate)

    assert cryptocurrency_action(1) == "Do nothing"


def test_do_nothing_if_095(monkeypatch: Any) -> None:
    def mock_rate(*args, **kwargs) -> float:
        return 0.95

    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", mock_rate)

    assert cryptocurrency_action(1) == "Do nothing"
