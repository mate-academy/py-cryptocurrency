from app.main import get_exchange_rate_prediction, cryptocurrency_action


def test_rate_105_buy_cryptocurrency() -> None:
    current_rate = 1.0
    prediction_rate = get_exchange_rate_prediction(current_rate)
    result = cryptocurrency_action(current_rate)
    if prediction_rate / current_rate > 1.05:
        assert result == "Buy more cryptocurrency"
    elif prediction_rate / current_rate < 0.95:
        assert result == "Sell all your cryptocurrency"
    else:
        assert result == "Do nothing"


def test_rate_105_percent_do_nothing() -> None:
    current_rate = 1.0
    prediction_rate = get_exchange_rate_prediction(current_rate)
    assert prediction_rate / current_rate != 1.05, (
        "You should not buy cryptocurrency when "
        "prediction_rate / current_rate == 1.05"
    )
