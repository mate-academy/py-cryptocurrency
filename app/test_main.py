import pytest
from app import main


@pytest.fixture
def mocked_get_exchange_rate_prediction(
    monkeypatch: pytest.MonkeyPatch
) -> callable:
    def mock_get_exchange_rate_prediction(
        exchange_rate: float
    ) -> float:
        return exchange_rate * 1.1
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    return mock_get_exchange_rate_prediction


def test_cryptocurrency_action_buy(
    mocked_get_exchange_rate_prediction: pytest.MonkeyPatch
) -> None:
    current_rate = 100
    action = main.cryptocurrency_action(current_rate)
    assert action == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: float) -> float:
        return exchange_rate * 0.9
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    current_rate = 100
    action = main.cryptocurrency_action(current_rate)
    assert action == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(
    monkeypatch: pytest.MonkeyPatch
) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: float) -> float:
        return exchange_rate * 1.0
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    current_rate = 100
    action = main.cryptocurrency_action(current_rate)
    assert action == "Do nothing"


def test_rate_105_percent_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: float) -> float:
        return exchange_rate * 1.05
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    current_rate = 100
    action = main.cryptocurrency_action(current_rate)
    assert action == "Do nothing"


def test_rate_95_percent_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(exchange_rate: float) -> float:
        return exchange_rate * 0.95
    monkeypatch.setattr(
        main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    current_rate = 100
    action = main.cryptocurrency_action(current_rate)
    assert action == "Do nothing"
