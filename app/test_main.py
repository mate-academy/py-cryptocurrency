from _pytest.monkeypatch import MonkeyPatch

from app.main import cryptocurrency_action
from typing import Union


def test_return_buy_more(monkeypatch: MonkeyPatch) -> None:
    def mock_exchange_rate(rate: Union[int, float]) -> float:
        return 0.6574436

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_exchange_rate)
    assert cryptocurrency_action(0.4843142) == "Buy more cryptocurrency"


def test_return_sell_all(monkeypatch: MonkeyPatch) -> None:
    def mock_exchange_rate(rate: Union[int, float]) -> float:
        return 0.3245354325

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_exchange_rate)
    assert cryptocurrency_action(0.4843142) == "Sell all your cryptocurrency"


def test_return_do_nothing(monkeypatch: MonkeyPatch) -> None:
    def mock_exchange_rate(rate: Union[int, float]) -> float:
        return 0.4954453

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_exchange_rate)
    assert cryptocurrency_action(0.4987642) == "Do nothing"
