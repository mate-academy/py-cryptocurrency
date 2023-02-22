from app.main import cryptocurrency_action


def test_sell_all_cryptocurrency(monkeypatch: object) -> None:
    def mock_exchange_rate_prediction(current_rate: float) -> float:
        return current_rate * 0.95

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_exchange_rate_prediction
    )

    result = cryptocurrency_action(100)
    assert (result != "Sell all your cryptocurrency")


def test_buy_more_cryptocurrency(monkeypatch: object) -> None:
    def mock_exchange_rate_prediction(current_rate: float) -> float:
        return current_rate * 1.05

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_exchange_rate_prediction
    )

    result = cryptocurrency_action(100)
    assert (result != "Buy more cryptocurrency")
