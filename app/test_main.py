import pytest
import app.main


@pytest.mark.parametrize(
    "current_rate,exchange_rate_change_percentage,result",
    [
        (1.36, 10, "Buy more cryptocurrency"),
        (1.36, 5.1, "Buy more cryptocurrency"),
        (1.36, 5, "Do nothing"),
        (1.36, -5, "Do nothing"),
        (1.36, -5.1, "Sell all your cryptocurrency"),
        (0.46, 4, "Do nothing"),
        (0.46, 6, "Buy more cryptocurrency"),
        (5.55, 10, "Buy more cryptocurrency"),
        (1.36, 0, "Do nothing"),
        (1.36, -10, "Sell all your cryptocurrency")
    ]
)
def test_cryptocurrency_action(
        monkeypatch: pytest.MonkeyPatch,
        current_rate: int | float,
        exchange_rate_change_percentage: int,
        result: str
) -> None:

    def fake_get_exchange_rate_prediction(
            exchange_rate: int | float
    ) -> float:

        return exchange_rate * (1 + exchange_rate_change_percentage / 100)

    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        fake_get_exchange_rate_prediction
    )

    assert (app.main.cryptocurrency_action(current_rate) == result), \
        (f"Failed: current rate = {current_rate}, "
         f"%change {exchange_rate_change_percentage}")
