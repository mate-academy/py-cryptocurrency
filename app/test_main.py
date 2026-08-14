from app.main import cryptocurrency_action
from typing import Any


def test_cryptocurrency_action_buy_more(monkeypatch: Any) -> None:
    """Test that the function returns "Buy more cryptocurrency"
    if predicted rate is >5% higher."""
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: exchange_rate * 1.06
    )
    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(monkeypatch: Any) -> None:
    """Test that the function returns "Sell all your cryptocurrency"
    if predicted rate is >5% lower."""
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: exchange_rate * 0.94
    )
    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(monkeypatch: Any) -> None:
    """Test that the function returns "Do nothing" if difference is <=5%."""
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: exchange_rate * 1.02
    )
    assert cryptocurrency_action(100.0) == "Do nothing"


def test_cryptocurrency_action_exact_5_percent_buy(monkeypatch: Any) -> None:
    """Test that the function returns "Do nothing"
    if predicted rate is exactly 5% higher."""
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: exchange_rate * 1.05
    )
    assert cryptocurrency_action(100.0) == "Do nothing"


def test_cryptocurrency_action_exact_5_percent_sell(monkeypatch: Any) -> None:
    """Test that the function returns "Do nothing"
    if predicted rate is exactly 5% lower."""
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: exchange_rate * 0.95
    )
    assert cryptocurrency_action(100.0) == "Do nothing"
