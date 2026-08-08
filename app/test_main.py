import pytest
import app.main as main


def test_buy_more_cryptocurrency(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda rate: rate * 1.10,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda rate: rate * 0.80,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Sell all your cryptocurrency"


def test_do_nothing_small_increase(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda rate: rate * 1.03,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


def test_do_nothing_small_decrease(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda rate: rate * 0.97,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


def test_boundary_exactly_plus_five_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda rate: rate * 1.05,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"


def test_boundary_exactly_minus_five_percent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda rate: rate * 0.95,
    )

    result = main.cryptocurrency_action(100)

    assert result == "Do nothing"
