from _pytest.monkeypatch import MonkeyPatch
from app.main import cryptocurrency_action


def test_action_if_exchange_rate_difference_not_so_big_from_current(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 104.0
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_action_if_exchange_rate_difference_lower_than_current(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 90.0
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_action_if_exchange_rate_difference_higher_than_current(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 110.0
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_action_if_exchange_rate_equal_95(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 95.0
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_action_if_exchange_rate_equal_105(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100.0
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda _: 105.0
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
