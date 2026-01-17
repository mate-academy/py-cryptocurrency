import pytest
import app.main as main
from app.main import cryptocurrency_action


def test_buy_case(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_fn(current_rate: int) -> int:
        return 106

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        fake_fn,
    )

    crypto: str = cryptocurrency_action(100)

    assert crypto == "Buy more cryptocurrency"


def test_sell_case(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_fn(current_rate: int) -> int:
        return 94

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        fake_fn,
    )

    crypto: str = cryptocurrency_action(100)

    assert crypto == "Sell all your cryptocurrency"


def test_do_nothing_upper(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_fn(current_rate: int) -> int:
        return 105

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        fake_fn,
    )

    crypto: str = cryptocurrency_action(100)

    assert crypto == "Do nothing"


def test_do_nothing_lower(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_fn(current_rate: int) -> int:
        return 95

    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        fake_fn,
    )

    crypto: str = cryptocurrency_action(100)

    assert crypto == "Do nothing"
