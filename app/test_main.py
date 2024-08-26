from app import main
from _pytest.monkeypatch import MonkeyPatch


def test_rate_105_percent_do_nothing(monkeypatch: MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(
        current_rate: float
    ) -> float:
        return current_rate * 1.05

    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", mock_get_exchange_rate_prediction
    )
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing", (
        "You should not buy cryptocurrency when "
        "prediction_rate / current_rate == 1.05"
    )


def test_rate_95_percent_do_nothing(monkeypatch: MonkeyPatch) -> None:
    def mock_get_exchange_rate_prediction(
        current_rate: float
    ) -> float:
        return current_rate * 0.95

    monkeypatch.setattr(
        main, "get_exchange_rate_prediction", mock_get_exchange_rate_prediction
    )
    result = main.cryptocurrency_action(100)
    assert result == "Do nothing", (
        "You should not sell cryptocurrency when "
        "prediction_rate / current_rate == 0.95"
    )
