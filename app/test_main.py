from app import main
from typing import Union
import pytest


def mock_get_exchange_rate_prediction_buy_more(
    exchange_rate: Union[int, float]
) -> float:
    return exchange_rate * 1.1  # Mocked to always predict an increase


def mock_get_exchange_rate_prediction_sell_all(
    exchange_rate: Union[int, float]
) -> float:
    return exchange_rate * 0.9  # Mocked to always predict a decrease


def mock_get_exchange_rate_prediction_do_nothing(
    exchange_rate: Union[int, float]
) -> float:
    return exchange_rate  # Mocked to always predict no change


def mock_get_exchange_rate_prediction_95(
    exchange_rate: Union[int, float]
) -> float:
    return exchange_rate * 0.95  # Mocked to always predict a 5% decrease


def mock_get_exchange_rate_prediction_105(
    exchange_rate: Union[int, float]
) -> float:
    return exchange_rate * 1.05  # Mocked to always predict a 5% increase


def test_cryptocurrency_action_buy_more(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_buy_more
    )
    action = main.cryptocurrency_action(100.0)
    assert action == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_sell_all
    )
    action = main.cryptocurrency_action(100.0)
    assert action == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_do_nothing
    )
    action = main.cryptocurrency_action(100.0)
    assert action == "Do nothing"


def test_cryptocurrency_action_edge_case_95(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_95
    )
    action = main.cryptocurrency_action(100.0)
    assert action == "Do nothing"


def test_cryptocurrency_action_edge_case_105(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction_105
    )
    action = main.cryptocurrency_action(100.0)
    assert action == "Do nothing"
