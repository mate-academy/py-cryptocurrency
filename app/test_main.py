from pytest import MonkeyPatch
from app.main import cryptocurrency_action


def test_buy_when_prediction_more_than_5_percent_higher(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 106,
    )
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


def test_sell_when_prediction_more_than_5_percent_lower(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 94,
    )
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


def test_do_nothing_when_prediction_exactly_5_percent_higher(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 105,
    )
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


def test_do_nothing_when_prediction_exactly_5_percent_lower(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 95,
    )
    result = cryptocurrency_action(100)
    assert result == "Do nothing"


def test_do_nothing_when_difference_small(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x: 102,
    )
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
