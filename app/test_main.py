import pytest
from typing import Callable
import app.main as main_module


@pytest.mark.parametrize(
    "current_rate, excepted_result, mock_exchange_rate", [
        pytest.param(
            100,
            "Buy more cryptocurrency",
            lambda exchange_rate: 110,
            id="You buy crypto!"
        ),
        pytest.param(
            100,
            "Sell all your cryptocurrency",
            lambda exchange_rate: 90,
            id="You sell crypto!"
        ),
        pytest.param(
            100,
            "Do nothing",
            lambda exchange_rate: 105,
            id="You do nothing!"
        ),
        pytest.param(
            100,
            "Do nothing",
            lambda exchange_rate: 95,
            id="You do nothing!"
        )
    ]
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: int | float,
        excepted_result: str,
        mock_exchange_rate: Callable
) -> None:
    monkeypatch.setattr(
        main_module,
        "get_exchange_rate_prediction",
        mock_exchange_rate
    )
    assert main_module.cryptocurrency_action(current_rate) == excepted_result
