import pytest

from app.main import cryptocurrency_action


def make_mock_get_exchange_rate_prediction(predicted_rate: float) -> callable:
    return lambda _: predicted_rate


@pytest.mark.parametrize(
    "current_rate,change_multiplier,expected_result",
    (
        (100, 1.05, "Do nothing"),
        (100, 0.95, "Do nothing"),
        (100, 1.51, "Buy more cryptocurrency"),
        (100, 0.94, "Sell all your cryptocurrency"),
    ),
    ids=(
        "should do nothing if growth rating is on the buy limit",
        "should do nothing if drop rating is on the sell limit",
        "should buy if growth rating us up of buy limit",
        "should sell if drop rating is under sell limit"
    )
)
def test_cryptocurrency_action(
        current_rate: int,
        change_multiplier: float,
        expected_result: str,
        monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        make_mock_get_exchange_rate_prediction(
            current_rate * change_multiplier
        )
    )
    assert cryptocurrency_action(current_rate) == expected_result
    monkeypatch.delattr("app.main.get_exchange_rate_prediction")
