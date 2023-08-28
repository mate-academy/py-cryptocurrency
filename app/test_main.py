import pytest

from typing import Callable

from pytest import MonkeyPatch

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "mock_get_exchange_rate_prediction, expected_result",
    [
        pytest.param(
            lambda rate: rate / 0.3,
            "Buy more cryptocurrency",
            id="should print Buy more cryptocurrency, if predicted exchange"
        ),
        pytest.param(
            lambda rate: rate * 0.7,
            "Sell all your cryptocurrency",
            id="should print Sell all your cryptocurrency if predicted",
        ),
        pytest.param(
            lambda rate: rate + rate * 0.05,
            "Do nothing",
            id="should print Do nothing, if difference is not that much.",
        ),
        pytest.param(
            lambda rate: round((rate * 0.95), 2),
            "Do nothing",
            id="should print Do nothing, if difference is not that much.",
        ),
    ]
)
def test_cryptocurrency(
    monkeypatch: MonkeyPatch,
    mock_get_exchange_rate_prediction: Callable,
    expected_result: str,
) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    assert cryptocurrency_action(25) == expected_result
