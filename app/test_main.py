from typing import Any, Union

from app.main import cryptocurrency_action


def test_buy_more_cryptocurrency(monkeypatch: Any) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]) -> float:
        return 1.06
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    current_rate = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: Any) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]) -> float:
        return 0.94
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    current_rate = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_do_nothing(monkeypatch: Any) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]) -> float:
        return 1.05

    def mock_get_exchange_rate_prediction2(
            exchange_rate: Union[int, float]) -> float:
        return 0.95

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)
    current_rate = 1.00
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction2)
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
