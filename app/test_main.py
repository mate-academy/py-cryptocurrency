from typing import Union

import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "predicted_rate,current_rate,expected_result",
    [
        (1.1, 1, "Buy more cryptocurrency"),
        (0.8, 1 , "Sell all your cryptocurrency"),
        (1, 1, "Do nothing"),
        (0.95, 1, "Do nothing"),
        (1.05, 1, "Do nothing"),
    ],
    ids=[
        "should return 'Buy more cryptocurrency' if rate > 5%",
        "should return 'Sell all your cryptocurrency' if rate < 0.95",
        "should return 'Do nothing' if difference is not that much",
        "should return 'Do nothing' if predicted_rate = 0.95",
        "should return 'Do nothing' if predicted_rate = 1.05"
    ]
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        predicted_rate: Union[int, float],
        current_rate: Union[int, float],
        expected_result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda x : predicted_rate
    )
    assert cryptocurrency_action(current_rate) == expected_result
