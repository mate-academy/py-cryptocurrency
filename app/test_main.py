import pytest
from typing import Union


from app.main import cryptocurrency_action


def test_cryptocurrency_action_income_increase(
    monkeypatch: pytest.MonkeyPatch
) -> None:

    def predicted_exchange_over_5_positive(
        current_rate: Union[int, float]
    ) -> float:
        return current_rate * 1.05

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        predicted_exchange_over_5_positive
    )

    assert (
        cryptocurrency_action(100) == "Buy more cryptocurrency"
    ), "On income increase more than 5%, should advise to buy"


def test_cryptocurrency_action_income_decrease(
    monkeypatch: pytest.MonkeyPatch
) -> None:

    def predicted_exchange_over_5_negative(
        current_rate: Union[int, float]
    ) -> float:
        return current_rate * 0.95

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        predicted_exchange_over_5_negative
    )

    assert (
        cryptocurrency_action(100) == "Sell all your cryptocurrency"
    ), "On income decrease less than 5%, should advise to sell"


def test_cryptocurrency_action_irrelevant_up(
    monkeypatch: pytest.MonkeyPatch
) -> None:

    def predicted_exchange_little_increase(
        current_rate: Union[int, float]
    ) -> float:
        return current_rate * 1.01

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        predicted_exchange_little_increase
    )

    assert (
        cryptocurrency_action(100) == "Do nothing"
    ), "On very little income, advises to do nothing"


def test_cryptocurrency_action_irrelevant_down(
    monkeypatch: pytest.MonkeyPatch
) -> None:

    def predicted_exchange_little_loss(
        current_rate: Union[int, float]
    ) -> float:
        return current_rate * 0.99

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        predicted_exchange_little_loss
    )

    assert (
        cryptocurrency_action(100) == "Do nothing"
    ), "On very little loss, advises to do nothing"
