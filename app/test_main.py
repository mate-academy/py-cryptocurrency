import pytest

from app import main


def test_buy_more_when_prediction_more_than_5_percent_higher(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda current_rate: 106
    )
    assert (
        main.cryptocurrency_action(100) == "Buy more cryptocurrency"
    )


def test_sell_all_when_prediction_more_than_5_percent_lower(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda current_rate: 94
    )
    assert (
        main.cryptocurrency_action(100) == "Sell all your cryptocurrency"
    )


def test_do_nothing_when_prediction_equal_to_current(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda current_rate: 100
    )
    assert main.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_at_exact_5_percent_higher_boundary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda current_rate: 105
    )
    assert main.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_at_exact_5_percent_lower_boundary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda current_rate: 95
    )
    assert main.cryptocurrency_action(100) == "Do nothing"


def test_buy_more_just_above_5_percent_boundary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda current_rate: 105.01
    )
    assert (
        main.cryptocurrency_action(100) == "Buy more cryptocurrency"
    )


def test_sell_all_just_below_5_percent_boundary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", lambda current_rate: 94.99
    )
    assert (
        main.cryptocurrency_action(100) == "Sell all your cryptocurrency"
    )
