import pytest

from app.main import cryptocurrency_action


def test_cryptocurrency_action_when_exchange_rate_increases(
    monkeypatch: pytest.MonkeyPatch,
) -> None:

    def mock_get_exchange_rate_prediction(exchange_rate: int) -> float:
        return exchange_rate * 1.06

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction,
    )

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action_when_exchange_rate_decreases(
    monkeypatch: pytest.MonkeyPatch,
) -> None:

    def mock_get_exchange_rate_prediction(exchange_rate: int) -> float:
        return exchange_rate * 0.94

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction,
    )

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_when_exchange_rate_stays_same(
    monkeypatch: pytest.MonkeyPatch,
) -> None:

    def mock_get_exchange_rate_prediction(exchange_rate: int) -> float:
        return exchange_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction,
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action_when_exchange_rate_exactly_95_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:

    def mock_get_exchange_rate_prediction(exchange_rate: int) -> float:
        return exchange_rate * 0.95

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction,
    )

    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action_when_exchange_rate_exactly_105_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:

    def mock_get_exchange_rate_prediction(exchange_rate: int) -> float:
        return exchange_rate * 1.05

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction,
    )

    assert cryptocurrency_action(100) == "Do nothing"
