from typing import Union

import app
from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy(monkeypatch: object) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]
    ) -> float:
        return 110

    monkeypatch.setattr(app.main,
                        "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_cryptocurrency_action_do_nothing_105(monkeypatch: object) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]
    ) -> float:
        return 105

    monkeypatch.setattr(app.main,
                        "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    assert cryptocurrency_action(100) == "Do nothing"


def test_cryptocurrency_action_sell(monkeypatch: object) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]
    ) -> float:
        return 94

    monkeypatch.setattr(app.main,
                        "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing_95(monkeypatch: object) -> None:
    def mock_get_exchange_rate_prediction(
            exchange_rate: Union[int, float]
    ) -> float:
        return 95

    monkeypatch.setattr(app.main,
                        "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    assert cryptocurrency_action(100) == "Do nothing"
