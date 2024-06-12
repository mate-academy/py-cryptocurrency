import pytest

from app import main


def test_rate_95_percent_do_nothing(monkeypatch):
    def rate_95_sell_cryptocurrency(current_rate):
        from app.main import get_exchange_rate_prediction
        prediction_rate = get_exchange_rate_prediction(current_rate)
        if prediction_rate / current_rate > 1.05:
            return "Buy more cryptocurrency"
        if prediction_rate / current_rate <= 0.95:
            return "Sell all your cryptocurrency"
        return "Do nothing"

    monkeypatch.setattr(
        main, "cryptocurrency_action", rate_95_sell_cryptocurrency
    )

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1, (
        "You should not sell cryptocurrency when "
        "prediction_rate / current_rate == 0.95"
    )


def test_rate_105_percent_do_nothing(monkeypatch):
    def rate_105_buy_cryptocurrency(current_rate):
        from app.main import get_exchange_rate_prediction
        prediction_rate = get_exchange_rate_prediction(current_rate)
        if prediction_rate / current_rate >= 1.05:
            return "Buy more cryptocurrency"
        if prediction_rate / current_rate < 0.95:
            return "Sell all your cryptocurrency"
        return "Do nothing"

    monkeypatch.setattr(
        main, "cryptocurrency_action", rate_105_buy_cryptocurrency
    )

    test_result = pytest.main(["app/test_main.py"])
    assert test_result.value == 1, (
        "You should not buy cryptocurrency when "
        "prediction_rate / current_rate == 1.05"
    )
