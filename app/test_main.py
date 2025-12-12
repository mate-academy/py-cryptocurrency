import pytest


from app.main import cryptocurrency_action

current_rate = 100.0


def test_cryptocurrency_action_buy(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 105.01
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rate: 94.99
    )
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


@pytest.mark.parametrize(
    "predicted_rate, expected_action",
    [
        (105.00, "Do nothing"),
        (100.00, "Do nothing"),
        (95.01, "Do nothing"),
        (95.00, "Do nothing"),
    ]
)
def test_cryptocurrency_action_action_nothing(
        monkeypatch: pytest.MonkeyPatch,
        predicted_rate: float,
        expected_action: str
) -> None:
    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        lambda rat: predicted_rate
    )
    result = cryptocurrency_action(current_rate)
    assert result == expected_action
