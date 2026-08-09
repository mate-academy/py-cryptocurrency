import pytest
from app.main import cryptocurrency_action
from _pytest.monkeypatch import MonkeyPatch


def test_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda *args: 105.1
    )
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda *args: 94.9
    )
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_if_rate_is_almost_the_same(
        monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda *args: 104.9
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_if_rate_is_same(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda *args: 100
    )
    assert cryptocurrency_action(100) == "Do nothing"


@pytest.mark.parametrize(
    "current_rate, predicted_rate, expected_action",
    [
        (100, 105.1, "Buy more cryptocurrency"),
        (100, 94.9, "Sell all your cryptocurrency"),
        (100, 104.9, "Do nothing"),
        (100, 95.1, "Do nothing"),
        (100, 100, "Do nothing"),
        (50, 52.51, "Buy more cryptocurrency"),
        (50, 55, "Buy more cryptocurrency"),
        (10, 10.51, "Buy more cryptocurrency"),
        (10, 12, "Buy more cryptocurrency"),
        (10, 9.49, "Sell all your cryptocurrency"),
        (100, 85, "Sell all your cryptocurrency"),
    ],
)
def test_cryptocurrency_action_parametrized(
        monkeypatch: MonkeyPatch,
        current_rate: int,
        predicted_rate: float,
        expected_action: str,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda *args: predicted_rate,
    )
    assert cryptocurrency_action(current_rate) == expected_action


def test_rate_105_percent_do_nothing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda *args: 105
    )
    assert cryptocurrency_action(100) == "Do nothing"


def test_rate_95_percent_do_nothing(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", lambda *args: 95
    )
    assert cryptocurrency_action(100) == "Do nothing"
