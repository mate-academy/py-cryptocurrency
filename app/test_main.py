import app.main as main
import pytest
from typing import Callable


@pytest.mark.parametrize(
    "mock_function, expected_action",
    [
        pytest.param(
            lambda rate: rate / 0.5, "Buy more cryptocurrency", id="Buy action"
        ),
        pytest.param(
            lambda rate: rate * 0.5,
            "Sell all your cryptocurrency",
            id="Sell action",
        ),
        pytest.param(
            lambda rate: rate + rate * 0.05,
            "Do nothing",
            id="Do nothing action when rate is 5% higher",
        ),
        pytest.param(
            lambda rate: round((rate * 0.95), 2),
            "Do nothing",
            id="Do nothing action when rate is 5% lower",
        ),
    ],
)
def test_cryptocurrency_action_with_parametrized_mocks(
    mock_function: Callable,
    expected_action: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """
    Test that cryptocurrency_action returns the expected action
    """
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_function)
    assert main.cryptocurrency_action(10) == expected_action
