from unittest.mock import patch


@patch("app.main.get_exchange_rate_prediction")
@patch("app.main.cryptocurrency_action")
def test_get_exchange_rate_prediction(mock_prediction_rate: int | float,
                                      mock_current_rate: int | float
                                      ) -> str:
    if (mock_prediction_rate > mock_current_rate
            + (mock_current_rate / 100 * 5)):
        return "Buy more cryptocurrency"
    elif (mock_prediction_rate > mock_current_rate
          - (mock_current_rate / 100 * 5)):
        return "Sell all your cryptocurrency"
    return "Do nothing"
