import pytest
from app import main


@pytest.mark.parametrize(
    "prediction_factor, expected_action",
    [
        pytest.param(1.06, "Buy more cryptocurrency", id="1.06_buy"),
        pytest.param(1.05, "Do nothing", id="1.05_nothing"),
        pytest.param(1.00, "Do nothing", id="1.00_nothing"),
        pytest.param(0.95, "Do nothing", id="0.95_nothing"),
        pytest.param(0.94, "Sell all your cryptocurrency", id="0.94_sell"),
    ]
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    prediction_factor: float,
    expected_action: str,
) -> None:
    current_rate = 100
    prediction_rate = current_rate * prediction_factor

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        lambda x: prediction_rate
    )

    assert main.cryptocurrency_action(current_rate) == expected_action
