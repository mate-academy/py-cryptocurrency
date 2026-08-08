from app.main import cryptocurrency_action
from pytest import MonkeyPatch


def test_when_crypto_rate_is_the_same(
        monkeypatch: "MonkeyPatch"
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 10.6)

    assert cryptocurrency_action(10) == "Buy more cryptocurrency"


def test_when_crypto_rate_is_more_than_5percent_higher(
        monkeypatch: "MonkeyPatch"
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 9.4)

    assert cryptocurrency_action(10) == "Sell all your cryptocurrency"


def test_when_crypto_rate_is_not_more_than_5percent_more(
        monkeypatch: "MonkeyPatch"
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 10.5)

    assert cryptocurrency_action(10) == "Do nothing"


def test_when_crypto_rate_is_not_more_than_5percent_less(
        monkeypatch: "MonkeyPatch"
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda x: 9.5)

    assert cryptocurrency_action(10) == "Do nothing"
