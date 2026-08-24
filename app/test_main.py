from app import main


def test_sell_with_float(monkeypatch: callable) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.20)
    assert main.cryptocurrency_action(1.50) == "Sell all your cryptocurrency"


def test_buy_with_int(monkeypatch: callable) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1)
    assert main.cryptocurrency_action(0.8) == "Buy more cryptocurrency"


def test_do_nothing(monkeypatch: callable) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.25)
    assert main.cryptocurrency_action(1.25) == "Do nothing"


def test_5_percent_higher_do_nothing(monkeypatch: callable) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 1.05)
    assert main.cryptocurrency_action(1) == "Do nothing"


def test_5_percent_lower_do_nothing(monkeypatch: callable) -> None:
    monkeypatch.setattr(main, "get_exchange_rate_prediction", lambda x: 0.95)
    assert main.cryptocurrency_action(1) == "Do nothing"
