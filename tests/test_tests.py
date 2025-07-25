import pytest
import app.main as main


def test_rate_95_percent_do_nothing(monkeypatch):
    def mock_prediction(_):
        return 95.0  # exactly 95% of 100

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    result = main.cryptocurrency_action(100.0)
    assert result == "Do nothing", (
        "You should not sell cryptocurrency when prediction_rate / current_rate == 0.95"
    )


def test_rate_105_percent_do_nothing(monkeypatch):
    def mock_prediction(_):
        return 105.0  # exactly 105% of 100

    monkeypatch.setattr(main, "get_exchange_rate_prediction", mock_prediction)
    result = main.cryptocurrency_action(100.0)
    assert result == "Do nothing", (
        "You should not buy cryptocurrency when prediction_rate / current_rate == 1.05"
    )
