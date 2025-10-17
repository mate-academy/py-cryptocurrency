from _pytest.monkeypatch import MonkeyPatch
from app import main


def test_buy_more_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    def mock_prediction(rate: float) -> float:
        return rate * 1.051  # Just above 5% increase
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_all_cryptocurrency(monkeypatch: MonkeyPatch) -> None:
    def mock_prediction(rate: float) -> float:
        return rate * 0.949  # Just below 5% decrease
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_upper_boundary(monkeypatch: MonkeyPatch) -> None:
    def mock_prediction(rate: float) -> float:
        return rate * 1.05  # Exactly 5% increase
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert main.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_lower_boundary(monkeypatch: MonkeyPatch) -> None:
    def mock_prediction(rate: float) -> float:
        return rate * 0.95  # Exactly 5% decrease
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert main.cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_middle(monkeypatch: MonkeyPatch) -> None:
    def mock_prediction(rate: float) -> float:
        return rate * 1.02  # Within ±5% range
    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert main.cryptocurrency_action(100) == "Do nothing"
