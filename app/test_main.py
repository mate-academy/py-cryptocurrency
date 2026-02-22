from app.main import cryptocurrency_action
from _pytest.monkeypatch import MonkeyPatch


def test_buy_when_increase_more_than_5_percent(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100

    def mock_prediction(rate: float) -> float:
        return 105.01

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )

    assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"


def test_sell_when_decrease_more_than_5_percent(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100

    def mock_prediction(rate: float) -> float:
        return 94.99

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )

    assert (cryptocurrency_action(current_rate)
            == "Sell all your cryptocurrency")


def test_do_nothing_when_exactly_plus_5_percent(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100

    def mock_prediction(rate: float) -> float:
        return 105

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )

    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_when_exactly_minus_5_percent(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100

    def mock_prediction(rate: float) -> float:
        return 95

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )

    assert cryptocurrency_action(current_rate) == "Do nothing"


def test_do_nothing_when_change_within_range(
        monkeypatch: MonkeyPatch
) -> None:
    current_rate = 100

    def mock_prediction(rate: float) -> float:
        return 102

    monkeypatch.setattr(
        "app.main.get_exchange_rate_prediction",
        mock_prediction
    )

    assert cryptocurrency_action(current_rate) == "Do nothing"
