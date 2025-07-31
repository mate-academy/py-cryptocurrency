import pytest
from typing import Union
from app.main import cryptocurrency_action


def test_buy_more(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: 110)
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: 90)
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_upper_boundary(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: 105)
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_lower_boundary(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: 95)
    assert cryptocurrency_action(100) == "Do nothing"


@pytest.mark.parametrize(
    "predicted, expected",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (100, "Do nothing"),
    ],
)
def test_parametrized(monkeypatch: pytest.MonkeyPatch,
                      predicted: Union[int, float],
                      expected: Union[int, float]) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: predicted)
    assert cryptocurrency_action(100) == expected


def test_buy_with_float(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: 105.01)
    assert cryptocurrency_action(100.0) == "Buy more cryptocurrency"


def test_sell_with_float(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: 94.99)
    assert cryptocurrency_action(100.0) == "Sell all your cryptocurrency"


def test_zero_current_rate(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: 0)
    with pytest.raises(ZeroDivisionError):
        cryptocurrency_action(0)


def test_negative_current_rate(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        lambda rate: -110)
    # Логіка не визначена для від’ємних, перевіряємо, що виклик не падає
    result = cryptocurrency_action(-100)
    assert result in [
        "Buy more cryptocurrency",
        "Sell all your cryptocurrency",
        "Do nothing",
    ]
