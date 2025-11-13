from app.main import cryptocurrency_action


def test_buy_more(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * 1.06
    )
    result = cryptocurrency_action(100)
    assert result == "Buy more cryptocurrency"


def test_sell_all(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * 0.94
    )
    result = cryptocurrency_action(100)
    assert result == "Sell all your cryptocurrency"


def test_do_nothing(monkeypatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda current_rate: current_rate * 1.03
    )
    result = cryptocurrency_action(100)
    assert result == "Do nothing"
