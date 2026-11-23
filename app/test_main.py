from _pytest.monkeypatch import MonkeyPatch

import app.main as main


def test_prediction_rate_more_than_current(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda current_rate: 1.06)
    assert main.cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_prediction_rate_less_than_current(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda current_rate: 0.94)
    assert main.cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_prediction_rate_like_a_current(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda current_rate: 0.95)
    assert main.cryptocurrency_action(1) == "Do nothing"


def test_prediction_rate_like_a_current_second(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        lambda current_rate: 1.05)
    assert main.cryptocurrency_action(1) == "Do nothing"
