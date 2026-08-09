import pytest
from typing import Union
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, expected_action, expected_prediction",
    [
        (100, "Buy more cryptocurrency", 106),
        (100, "Sell all your cryptocurrency", 94),
        (100, "Do nothing", 100),
        (100, "Do nothing", 105),
        (100, "Do nothing", 95)
    ]
)
def test_cryptocurrency_action(
    current_rate: int,
    expected_action: str,
    expected_prediction: float,
    monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_get_exchange_rate_prediction(
        exchange_rate: Union[int, float]
    ) -> float:
        if expected_action == "Buy more cryptocurrency":
            return expected_prediction
        elif expected_action == "Sell all your cryptocurrency":
            return expected_prediction
        else:
            return expected_prediction

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )

    action = cryptocurrency_action(current_rate)
    assert action == expected_action
