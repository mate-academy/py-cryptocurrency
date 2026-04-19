from pytest import MonkeyPatch
from app.main import cryptocurrency_action


def test_cryptocurrency_action_then_increase(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 2
    )

    result = cryptocurrency_action(1)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_then_not_increase(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 0.5
    )

    result = cryptocurrency_action(1)
    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_then_all_stable(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 1
    )
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 1.05
    )
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 0.95
    )

    result = cryptocurrency_action(1)
    assert result == "Do nothing"


def test_cryptocurrency_action_then_high_limit(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 0.95
    )

    result = cryptocurrency_action(1)
    assert result == "Do nothing"


def test_cryptocurrency_action_then_lower_limit(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 1.05
    )

    result = cryptocurrency_action(1)
    assert result == "Do nothing"
