import pytest
from app.main import cryptocurrency_action


def mock_get_exchange_rate_prediction(current_rate: float) -> callable:
    def mock() -> float:
        return current_rate
    return mock


def test_buy_more_cryptocurrency(monkeypatch: pytest.MonkeyPatch
                                 ) -> None:
    current_rate = 100
    monkeypatch.setattr("app.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction(106))
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_buy_sell_cryptocurrency(monkeypatch: pytest.MonkeyPatch
                                 ) -> None:
    current_rate = 100
    monkeypatch.setattr("app.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction(94))
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_buy_difference_cryptocurrency1(monkeypatch: pytest.MonkeyPatch
                                        ) -> None:
    current_rate = 100
    monkeypatch.setattr("app.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction(104))
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_buy_difference_cryptocurrency2(monkeypatch: pytest.MonkeyPatch
                                        ) -> None:
    current_rate = 100
    monkeypatch.setattr("app.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction(96))
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
