from _pytest.monkeypatch import MonkeyPatch

from app.main import cryptocurrency_action


def test_should_buy_more_cryptocurrency(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 106.0,
    )

    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


def test_should_sell_all_cryptocurrency(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 94.0,
    )

    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


def test_should_do_nothing_when_difference_is_less_than_5_percent_up(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 104.0,
    )

    assert cryptocurrency_action(100.0) == "Do nothing"


def test_should_do_nothing_when_difference_is_less_than_5_percent_down(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 96.0,
    )

    assert cryptocurrency_action(100.0) == "Do nothing"


def test_should_do_nothing_when_difference_is_exactly_5_percent_up(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 105.0,
    )

    assert cryptocurrency_action(100.0) == "Do nothing"


def test_should_do_nothing_when_difference_is_exactly_5_percent_down(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 95.0,
    )

    assert cryptocurrency_action(100.0) == "Do nothing"
