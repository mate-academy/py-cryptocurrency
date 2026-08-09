from pytest import MonkeyPatch
from app.main import cryptocurrency_action


def test_exchange_rate_is_exactly_five_percent_more(monkeypatch: MonkeyPatch
                                                    ) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 105,
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_exchange_rate_is_exactly_five_percent_less(monkeypatch: MonkeyPatch
                                                    ) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 95,
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_difference_is_not_big(monkeypatch: MonkeyPatch
                               ) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 101,
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_exchange_rate_is_more(monkeypatch: MonkeyPatch
                               ) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 106,
    )

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_exchange_rate_is_less(monkeypatch: MonkeyPatch
                               ) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda exchange_rate: 94,
    )

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
