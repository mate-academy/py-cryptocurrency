import pytest
from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_prediction(current_rate: float) -> float:
        return current_rate * 1.10
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction)
    assert cryptocurrency_action(100) == (
        "Buy more cryptocurrency"
    )


def test_sell_all_cryptocurrency(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_prediction(current_rate: float) -> float:
        return current_rate * 0.90
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction)
    assert cryptocurrency_action(100) == (
        "Sell all your cryptocurrency"
    )


def test_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_prediction(current_rate: float) -> float:
        return current_rate * 1.03
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction)
    assert cryptocurrency_action(100) == (
        "Do nothing"
    )


def test_rate_105_percent_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_prediction(current_rate: float) -> float:
        return current_rate * 1.05
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction)
    assert cryptocurrency_action(100) == (
        "Do nothing"
    )


def test_rate_90_percent_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_prediction(current_rate: float) -> float:
        return current_rate * 0.95
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction)
    assert cryptocurrency_action(100) == (
        "Do nothing"
    )
