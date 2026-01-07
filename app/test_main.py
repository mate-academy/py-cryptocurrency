from _pytest.monkeypatch import MonkeyPatch

import app.main

from app.main import cryptocurrency_action


def test_cryptocurrency_action_if_predicted_rate_more_than_5_persent(
        monkeypatch: MonkeyPatch
) -> None:

    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda *args: 1.06
    )

    assert cryptocurrency_action(1) == "Buy more cryptocurrency"


def test_cryptocurrency_action_if_predicted_rate_is_more_by_5_persents(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda *args: 1.05
    )

    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_action_if_predicted_rate_almost_the_same(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda *args: 1.02
    )

    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_action_if_predicted_rate_is_less_by_5_persents(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda *args: 0.95
    )

    assert cryptocurrency_action(1) == "Do nothing"


def test_cryptocurrency_action_if_predicted_rate_less_than_5_persent(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        lambda *args: 0.94
    )

    assert cryptocurrency_action(1) == "Sell all your cryptocurrency"
