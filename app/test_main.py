import pytest
from app.main import cryptocurrency_action


def test_buy_more(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 106
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 94
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_increase(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 104
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_decrease(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 96
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_plus_5_percent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 105
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_exactly_minus_5_percent(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 95
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_zero_value() -> None:
    with pytest.raises(ValueError):
        cryptocurrency_action(0)


def test_negative_value() -> None:
    with pytest.raises(ValueError):
        cryptocurrency_action(-100)


def test_invalid_type() -> None:
    with pytest.raises(TypeError):
        cryptocurrency_action("100")
