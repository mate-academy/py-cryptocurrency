from pytest import MonkeyPatch
from app.main import cryptocurrency_action


def test_returns_buy_more_when_rate_increases(
        monkeypatch: MonkeyPatch) -> None:
    current_rate = 100
    predicted_rate = 106

    def mock_prediction(_float: float) -> float:
        return predicted_rate

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_prediction)
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_returns_sell_your_cryptocurrency_when_decrease(
        monkeypatch: MonkeyPatch) -> None:
    current_rate = 100
    predicted_rate = 94

    def mock_prediction(_: float) -> float:
        return predicted_rate

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_prediction)
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_returns_sell_all_when_rate_decrease_is_slightly_below_5_percent(
        monkeypatch: MonkeyPatch) -> None:
    current_rate = 100
    predicted_rate = 94.99

    def mock_prediction(_: float) -> float:
        return predicted_rate

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_prediction)
    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_returns_do_nothing_when_rate_increase_is_exactly_5_percent(
        monkeypatch: MonkeyPatch) -> None:
    current_rate = 100
    predicted_rate = 105

    def mock_prediction(_: float) -> float:
        return predicted_rate

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_prediction)
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"


def test_returns_do_nothing_when_rate_decrease_is_exactly_5_percent(
        monkeypatch: MonkeyPatch) -> None:
    current_rate = 100
    predicted_rate = 95

    def mock_prediction(_: float) -> float:
        return predicted_rate

    monkeypatch.setattr("app.main.get_exchange_rate_prediction",
                        mock_prediction)
    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
