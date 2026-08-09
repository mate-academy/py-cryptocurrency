from _pytest.monkeypatch import MonkeyPatch

from app import main


def test_cryptocurrency_action_when_to_buy_more(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 106)
    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action_when_to_sell_all(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 0.94)
    assert main.cryptocurrency_action(1) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_when_do_nothing(
        monkeypatch: MonkeyPatch
) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 0.95)
    assert main.cryptocurrency_action(1) == "Do nothing"

    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 105)
    assert main.cryptocurrency_action(100) == "Do nothing"
