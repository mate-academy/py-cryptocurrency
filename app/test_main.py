import pytest
import app.main as main


def test_should_sell_when_prediction_less_than_5_percent(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda rate: 94)

    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_should_do_nothing_when_change_within_5_percent(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda rate: 104)

    assert main.cryptocurrency_action(100) == "Do nothing"


def test_should_do_nothing_when_change_exactly_5_percent(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda rate: 105)

    assert main.cryptocurrency_action(100) == "Do nothing"


def test_should_buy_when_prediction_more_than_5_percent(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda rate: 106)

    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"
