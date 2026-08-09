import pytest
from app import main


def test_rate_95_percent_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that no action is taken when prediction rate is exactly 95% of the
    current rate."""

    def mock_get_exchange_rate_prediction(_: float) -> float:
        return 95  # Mock prediction rate exactly 95% of the current rate

    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    result = main.cryptocurrency_action(100)  # Current rate is 100
    assert result == "Do nothing", "You should not sell cryptocurrency when " \
                                   "prediction_rate / current_rate == 0.95"


def test_rate_105_percent_do_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that no action is taken when prediction rate is exactly 105% of the
    current rate."""

    def mock_get_exchange_rate_prediction(_: float) -> float:
        return 105  # Mock prediction rate exactly 105% of the current rate

    monkeypatch.setattr(main, "get_exchange_rate_prediction",
                        mock_get_exchange_rate_prediction)

    result = main.cryptocurrency_action(100)  # Current rate is 100
    assert result == "Do nothing", "You should not buy cryptocurrency when " \
                                   "prediction_rate / current_rate == 1.05"
