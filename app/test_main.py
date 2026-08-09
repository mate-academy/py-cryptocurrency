from collections.abc import Callable

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate,mock_get_exchange_rate,expected_result",
    [
        pytest.param(
            100,
            lambda *args: 94,
            "Sell all your cryptocurrency",
        ),
        pytest.param(
            100,
            lambda *args: 106,
            "Buy more cryptocurrency",
        ),
        pytest.param(
            100,
            lambda *args: 95,
            "Do nothing",
        ),
        pytest.param(
            100,
            lambda *args: 105,
            "Do nothing",
        ),
    ],
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: float,
    mock_get_exchange_rate: Callable,
    expected_result: str,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction", mock_get_exchange_rate
    )
    assert cryptocurrency_action(current_rate) == expected_result
