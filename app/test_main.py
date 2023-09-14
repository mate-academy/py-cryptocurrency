import pytest
from app import main
from typing import Any


def rate_105_buy_cryptocurrency(current_rate: int or float) -> str:
    prediction_rate = main.get_exchange_rate_prediction(current_rate)
    if prediction_rate / current_rate >= 1.05:
        return "Buy more cryptocurrency"
    if prediction_rate / current_rate < 0.95:
        return "Sell all your cryptocurrency"
    return "Do nothing"


def test_rate_105_percent_do_nothing(monkeypatch: Any) -> None:
    monkeypatch.setattr(
        main,
        "cryptocurrency_action",
        rate_105_buy_cryptocurrency
    )
    test_result = pytest.main(["app/test_main.py"])
    assert test_result == 0, (
        "You should not buy cryptocurrency when "
        "prediction_rate / current_rate == 1.05"
    )
