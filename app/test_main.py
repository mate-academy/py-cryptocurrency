import pytest

import app.main


monkeypatch = pytest.MonkeyPatch()


@pytest.fixture
def mock_get_exchange_rate(monkeypatch: pytest.MonkeyPatch,
                           rate: int | float,
                           multiplier: float) -> None:

    def get_rate(*args, **kwargs) -> int | float:
        return rate * multiplier

    monkeypatch.setattr(app.main, "get_exchange_rate_prediction", get_rate)


@pytest.mark.parametrize(
    "rate, multiplier, expected_result",
    [
        (15, 2, "Buy more cryptocurrency"),
        (15, 0.1, "Sell all your cryptocurrency"),
        (15, 1, "Do nothing"),
        (15, 1.05, "Do nothing"),
        (15, 0.95, "Do nothing"),
    ],
    ids=[
        "Get rate increase, with rise > 1.05",
        "Get rate decrease, with rise < 0.95",
        "Get rate with 95 < rise < 1.05",
        "Get rate with rise = 0.95",
        "Get rate with rise = 1.05",
    ]
)
def test_cryptocurrency_action_buy(rate: int | float,
                                   multiplier: float,
                                   expected_result: str,
                                   mock_get_exchange_rate: callable) -> None:
    assert app.main.cryptocurrency_action(rate) == expected_result
