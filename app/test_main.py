import pytest
import app.main as main


def test_boundary_95(monkeypatch: pytest.MonkeyPatch) -> None:
    current_rate: float = 100.0
    prediction_rate: float = 95.0

    def fake_prediction(_: float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        fake_prediction
    )
    result: str = main.cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_boundary_105(monkeypatch: pytest.MonkeyPatch) -> None:
    current_rate: float = 100.0
    prediction_rate: float = 105.0

    def fake_prediction(_: float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        fake_prediction
    )
    result: str = main.cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_buy(monkeypatch: pytest.MonkeyPatch) -> None:
    current_rate: float = 100.0
    prediction_rate: float = 106.0

    def fake_prediction(_: float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        fake_prediction
    )
    result: str = main.cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_sell(monkeypatch: pytest.MonkeyPatch) -> None:
    current_rate: float = 100.0
    prediction_rate: float = 94.0

    def fake_prediction(_: float) -> float:
        return prediction_rate

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        fake_prediction
    )
    result: str = main.cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"
