from typing import Callable, Union

import pytest
from pytest import MonkeyPatch

from app import main
from app.main import cryptocurrency_action


def mock_prediction(
    predicted_rate: float
) -> Callable[[Union[int, float]], float]:
    def _mock(_: Union[int, float]) -> float:
        return predicted_rate
    return _mock


BUY_CASES = [
    (100, 106.0),
    (200, 211.0),
]

SELL_CASES = [
    (100, 94.0),
    (200, 180.0),
]

DO_NOTHING_CASES = [
    (100, 105.0),
    (100, 95.0),
    (100, 100.0),
]


class TestCryptocurrencyAction:

    @pytest.mark.parametrize(
        ("current_rate", "predicted_rate"),
        BUY_CASES,
        ids=[
            "buy: 106 > 5% of 100",
            "buy: 211 > 5% of 200",
        ],
    )
    def test_buy_when_prediction_is_more_than_5_percent(
        self,
        current_rate: Union[int, float],
        predicted_rate: float,
        monkeypatch: MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            main,
            "get_exchange_rate_prediction",
            mock_prediction(predicted_rate)
        )
        result = cryptocurrency_action(current_rate)
        assert result == "Buy more cryptocurrency"
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        ("current_rate", "predicted_rate"),
        SELL_CASES,
        ids=[
            "sell: 94 < 95% of 100",
            "sell: 180 < 95% of 200",
        ],
    )
    def test_sell_when_prediction_is_less_than_5_percent(
        self,
        current_rate: Union[int, float],
        predicted_rate: float,
        monkeypatch: MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            main,
            "get_exchange_rate_prediction",
            mock_prediction(predicted_rate)
        )
        result = cryptocurrency_action(current_rate)
        assert result == "Sell all your cryptocurrency"
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        ("current_rate", "predicted_rate"),
        DO_NOTHING_CASES,
        ids=[
            "do nothing: 105 == 105% of 100",
            "do nothing: 95 == 95% of 100",
            "do nothing: no significant change",
        ],
    )
    def test_do_nothing_when_prediction_is_within_5_percent(
        self,
        current_rate: Union[int, float],
        predicted_rate: float,
        monkeypatch: MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            main,
            "get_exchange_rate_prediction",
            mock_prediction(predicted_rate)
        )
        result = cryptocurrency_action(current_rate)
        assert result == "Do nothing"
        assert isinstance(result, str)