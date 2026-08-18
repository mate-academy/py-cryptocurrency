from app import main
from app.main import cryptocurrency_action
from pytest import MonkeyPatch


def test_should_buy_when_prediction_is_more_than_five_percen_higher(
        monkeypatch: MonkeyPatch,) -> None:
    current_rate = 100

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda i: 106,
    )

    result = cryptocurrency_action(current_rate)

    assert result == "Buy more cryptocurrency"


def test_should_do_nothing_when_prediction_is_exactly_five_percent_higher(
        monkeypatch: MonkeyPatch,) -> None:
    current_rate = 100

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda i: 105,
    )

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"


def test_should_do_nothing_when_prediction_is_exactly_five_percent_lower(
        monkeypatch: MonkeyPatch,) -> None:
    current_rate = 100

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda i: 95,
    )

    result = cryptocurrency_action(current_rate)

    assert result == "Do nothing"


def test_should_sell_when_prediction_is_less_than_five_percen_higher(
        monkeypatch: MonkeyPatch,) -> None:
    current_rate = 100

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda i: 94,
    )

    result = cryptocurrency_action(current_rate)

    assert result == "Sell all your cryptocurrency"
