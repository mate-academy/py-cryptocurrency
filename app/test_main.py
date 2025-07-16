import pytest

from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "current_rate, predicted_rate, result",
    [
        (10, 10.5, "Do nothing"),
        (20, 21.1, "Buy more cryptocurrency"),
        (30, 28.5, "Do nothing"),
        (40, 37.8, "Sell all your cryptocurrency")
    ],
    ids=[
        "predicted rate equal to upper threshold",
        "predicted rate greater than upper threshold",
        "predicted rate equal to lower threshold",
        "predicted rate less than lower threshold",
    ]
)
def test_get_exchange_rate_prediction(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: float | int,
        predicted_rate: float | int,
        result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: predicted_rate
    )
    assert cryptocurrency_action(current_rate) == result
