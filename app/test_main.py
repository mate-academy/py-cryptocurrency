from app.main import cryptocurrency_action
from app import main


def test_buy_cryptocurrency(monkeypatch: object) -> None:

    def mock_prediction(mocked_exchange_rate: float) -> float:
        return 110

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_sell_cryptocurrency(monkeypatch: object) -> None:

    def mock_prediction(mocked_exchange_rate: float) -> float:
        return 90

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


def test_do_nothing_cryptocurrency(monkeypatch: object) -> None:

    def mock_prediction(mocked_exchange_rate: float) -> float:
        return 100

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_upper_bound_cryptocurrency(monkeypatch: object) -> None:

    def mock_prediction(mocked_exchange_rate: float) -> float:
        return 105

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert cryptocurrency_action(100) == "Do nothing"


def test_do_nothing_lower_bound_cryptocurrency(monkeypatch: object) -> None:

    def mock_prediction(mocked_exchange_rate: float) -> float:
        return 95

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    assert cryptocurrency_action(100) == "Do nothing"
