import pytest
from app import main


def prediction_rate_1(num) -> float:
    return 0.95


def prediction_rate_2(num) -> float:
    return 1.05


def prediction_rate_3(num) -> float:
    return 2.3


def prediction_rate_4(num) -> float:
    return 1.7


@pytest.mark.parametrize(
    "current_rate, prediction_rate, expected_result",
    [
        (
            1,
            prediction_rate_1,
            "Do nothing",
        ),
        (
            1,
            prediction_rate_2,
            "Do nothing"
        ),
        (
            2,
            prediction_rate_3,
            "Buy more cryptocurrency"
        ),
        (
            2,
            prediction_rate_4,
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
