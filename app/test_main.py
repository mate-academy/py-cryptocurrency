import pytest

from app import main


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        pytest.param(
            1,
            lambda num: 0.95,
            "Do nothing"
        ),
        pytest.param(
            1,
            lambda num: 1.05,
            "Do nothing"
        ),
        pytest.param(
            2,
            lambda num: 2.3,
            "Buy more cryptocurrency"
        ),
        pytest.param(
            2,
            lambda num: 1.7,
            "Sell all your cryptocurrency"
        )
    ]
)
def test_cryptocurrency_action(
    monkeypatch: pytest.MonkeyPatch,
    current_rate: int | float,
    prediction_rate: int | float,
    expected_result: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        prediction_rate
    )

    assert main.cryptocurrency_action(current_rate) == expected_result
