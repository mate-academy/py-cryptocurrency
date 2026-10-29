
import pytest

from app import main


def test_buy_more_cryptocurrency(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: 106,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: 94,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


def test_do_nothing_when_rate_is_unchanged(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: 100,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


def test_do_nothing_when_rate_increases_by_exactly_five_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: 105,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


def test_do_nothing_when_rate_decreases_by_exactly_five_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: 95,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


def test_do_nothing_when_rate_changes_by_less_than_five_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda current_rate: 103,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"
