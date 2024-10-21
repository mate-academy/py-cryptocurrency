from app import main
from app.main import cryptocurrency_action


def test_cryptocurrency_action_equal_buy(monkeypatch: None) -> None:
    def noting(current_rate: int | float) -> int | float:
        return current_rate * 1.05
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", noting
    )
    test = cryptocurrency_action(2)
    assert test == "Do nothing"


def test_cryptocurrency_action_equal_sell(monkeypatch: None) -> None:
    def noting(current_rate: int | float) -> int | float:
        return current_rate * 0.95
    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", noting
    )
    test = cryptocurrency_action(2)
    assert test == "Do nothing"
