import pytest

from app.main import cryptocurrency_action


def test_cryptocurrency_increase(monkeypatch: pytest.MonkeyPatch) -> None:
    def monkey_exchange(exchange_rate: int) -> int:
        return 106

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        monkey_exchange)

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_decrease(monkeypatch: pytest.MonkeyPatch) -> None:
    def monkey_exchange(exchange_rate: int) -> int:
        return 94

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        monkey_exchange)

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_do_nothing_with_95(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    def monkey_exchange(exchange_rate: int) -> int:
        return 95

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        monkey_exchange)

    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_do_nothing_with_105(
        monkeypatch: pytest.MonkeyPatch
) -> None:
    def monkey_exchange(exchange_rate: int) -> int:
        return 105

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        monkey_exchange)

    assert cryptocurrency_action(100) == "Do nothing"
