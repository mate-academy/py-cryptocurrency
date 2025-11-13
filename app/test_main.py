import pytest
from app import main


def test_high_rate_prediction(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.06)
    expected = "Buy more cryptocurrency"
    assert main.cryptocurrency_action(1.0) == expected


def test_low_rate_prediction(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 0.94)
    expected = "Sell all your cryptocurrency"
    assert main.cryptocurrency_action(1.0) == expected


def test_no_difference_in_middle_rate_prediction(
        monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.0)
    expected = "Do nothing"
    assert main.cryptocurrency_action(1.0) == expected


def test_exactly_095_rate_prediction(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 0.95)
    expected = "Do nothing"
    assert main.cryptocurrency_action(1.0) == expected


def test_exactly_105__rate_prediction(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.05)
    expected = "Do nothing"
    assert main.cryptocurrency_action(1.0) == expected


def test_exactly_102__rate_prediction(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.02)
    expected = "Do nothing"
    assert main.cryptocurrency_action(1.0) == expected
