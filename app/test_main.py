from app.main import cryptocurrency_action
import app.main


current_rate = 100


def test_buy_more_cryptocurrency_rate_110(monkeypatch: any) -> None:
    def mock_get_exchange_rate_prediction(current_rate: float) -> float:
        return 110
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_do_nothing_rate_105_upper_margin(monkeypatch: any) -> None:
    def mock_get_exchange_rate_prediction(current_rate: float) -> float:
        return 105
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_rate_95_lower_margin(monkeypatch: any) -> None:
    def mock_get_exchange_rate_prediction(current_rate: float) -> float:
        return 95
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_sell_all_your_cryptocurrency_rate_90(monkeypatch: any) -> None:
    def mock_get_exchange_rate_prediction(current_rate: float) -> float:
        return 90
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    assert cryptocurrency_action(
        current_rate
    ) == "Sell all your cryptocurrency"


def test_do_nothing_rate_98(monkeypatch: any) -> None:
    def mock_get_exchange_rate_prediction(current_rate: float) -> float:
        return 98
    monkeypatch.setattr(
        app.main,
        "get_exchange_rate_prediction",
        mock_get_exchange_rate_prediction
    )
    assert cryptocurrency_action(current_rate) == "Do nothing"
