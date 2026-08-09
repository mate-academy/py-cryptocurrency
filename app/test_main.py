import pytest
from app.main import cryptocurrency_action
from typing import Callable


def mock_get_exchange_rate_prediction(rate: float) -> float:
    return rate


def test_rate_95_percent_do_nothing(monkeypatch: Callable) -> None:
    def mock_get_exchange_rate_prediction(rate: float) -> float:
        return rate * 0.95

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_105_percent_do_nothing(monkeypatch: Callable) -> None:
    def mock_get_exchange_rate_prediction(rate: float) -> float:
        return rate * 1.05

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_more_than_105_percent_buy(monkeypatch: Callable) -> None:
    def mock_get_exchange_rate_prediction(rate: float) -> float:
        return rate * 1.06

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_rate_less_than_95_percent_sell(monkeypatch: Callable) -> None:
    def mock_get_exchange_rate_prediction(rate: float) -> float:
        return rate * 0.94

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


if __name__ == "__main__":
    pytest
