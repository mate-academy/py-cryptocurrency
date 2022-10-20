from app import main
from app.main import cryptocurrency_action


def test_should_return_to_buy_currency(monkeypatch: object) -> None:

    def mocked_prediction_rate(exchange_rate: int) -> int:
        return exchange_rate * 2

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mocked_prediction_rate
    )
    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


def test_should_return_to_sell_currency(monkeypatch: object) -> None:

    def mocked_prediction_rate(exchange_rate: int) -> int:
        return exchange_rate // 2

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mocked_prediction_rate
    )
    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


def test_should_return_to_do_nothing_if_equal_95(monkeypatch: object) -> None:

    def mocked_prediction_rate(exchange_rate: int) -> float:
        return exchange_rate * 0.95

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mocked_prediction_rate
    )
    assert cryptocurrency_action(2) == "Do nothing"


def test_should_return_to_do_nothing_if_equal_105(monkeypatch: object) -> None:

    def mocked_prediction_rate(exchange_rate: int) -> float:
        return exchange_rate * 1.05

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mocked_prediction_rate
    )
    assert cryptocurrency_action(2) == "Do nothing"
