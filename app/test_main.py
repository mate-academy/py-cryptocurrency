import pytest

from app.main import cryptocurrency_action
from typing import Union


def test_higher_rate(monkeypatch: pytest.MonkeyPatch) -> None:

    def mock_get_exchange_rate_prediction(exchange_rate: Union[int, float]) \
            -> float:
        return exchange_rate * 1.06

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    result = cryptocurrency_action(2.0)
    assert result == "Buy more cryptocurrency"


def test_lower_rate(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: Union[int, float]) \
            -> float:
        return exchange_rate * 0.94

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    result = cryptocurrency_action(2.0)
    assert result == "Sell all your cryptocurrency"


def test_same_rate(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: Union[int, float]) \
            -> float:
        return exchange_rate * 1

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    result = cryptocurrency_action(2.0)
    assert result == "Do nothing"


def test_five_percent_increase_rate(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: Union[int, float]) \
            -> float:
        return exchange_rate * 1.05

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    result = cryptocurrency_action(2.0)
    assert result == "Do nothing"


def test_five_percent_decrease_rate(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: Union[int, float]) \
            -> float:
        return exchange_rate * 0.95

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    result = cryptocurrency_action(2.0)
    assert result == "Do nothing"
