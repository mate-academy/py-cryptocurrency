import pytest
from app.main import cryptocurrency_action


def test_buy_more(monkeypatch):
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda rate: 110)
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all(monkeypatch):
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda rate: 90)
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_upper_boundary(monkeypatch):
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda rate: 105)
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_lower_boundary(monkeypatch):
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda rate: 95)
    assert cryptocurrency_action(100) == "Do nothing"


import pytest

@pytest.mark.parametrize(
    "predicted,expected",
    [
        (106, "Buy more cryptocurrency"),
        (94, "Sell all your cryptocurrency"),
        (100, "Do nothing"),
    ],
)
def test_parametrized(monkeypatch, predicted, expected):
    monkeypatch.setattr("app.main.get_exchange_rate_prediction", lambda rate: predicted)
    assert cryptocurrency_action(100) == expected
