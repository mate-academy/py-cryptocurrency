import pytest
from pytest import MonkeyPatch
from typing import Union

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,expected_result",
    [
        pytest.param(
            1.05,
            "Do nothing",
            id="function should return 'Do nothing' if "
               "'predicted_rate' is '1.05'",
        ),
        pytest.param(
            0.95,
            "Do nothing",
            id="function should return 'Do nothing' if "
               "'predicted_rate' is '0.95'",
        ),
        pytest.param(
            1.06,
            "Buy more cryptocurrency",
            id="function should return 'Buy more cryptocurrency' if "
               "'predicted_rate' more than '1.05'",
        ),
        pytest.param(
            0.94,
            "Sell all your cryptocurrency",
            id="function should return 'Sell all your cryptocurrency' if "
               "'predicted_rate' less than '0.95'",
        ),
    ],
)
def test_cryptocurrency_action_correct(
    monkeypatch: MonkeyPatch,
    predicted_rate: Union[int, float],
    expected_result: str,
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda *args, **kwargs: predicted_rate,
    )

    assert cryptocurrency_action(1) == expected_result
