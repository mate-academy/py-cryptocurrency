import pytest

from app import main


def test_buy_more_cryptocurrency_when_prediction_is_more_than_5_percent_higher(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def prediction(current_rate: float) -> float:
        return current_rate * 1.06

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        prediction,
    )

    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_crypto_when_prediction_is_more_than_5_percent_lower(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def prediction(current_rate: float) -> float:
        return current_rate * 0.94

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        prediction,
    )

    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "prediction_factor",
    [0.95, 1.0, 1.05],
)
def test_do_nothing_when_prediction_difference_is_not_more_than_5_percent(
    monkeypatch: pytest.MonkeyPatch,
    prediction_factor: float,
) -> None:
    def prediction(current_rate: float) -> float:
        return current_rate * prediction_factor

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        prediction,
    )

    assert main.cryptocurrency_action(100) == "Do nothing"
