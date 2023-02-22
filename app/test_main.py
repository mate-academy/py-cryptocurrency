from unittest.mock import patch
import app.test_main as main


@patch("app.test_main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_get_exchange_rate_prediction: None
                                 ) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.1
    assert main.cryptocurrency_action(1.0) == "Buy more cryptocurrency"


@patch("app.test_main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_get_exchange_rate_prediction: None
                                 ) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.9
    assert main.cryptocurrency_action(1.0) == "Sell all your cryptocurrency"


@patch("app.test_main.get_exchange_rate_prediction")
def test_do_nothing(mock_get_exchange_rate_prediction: None
                    ) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.03
    assert main.cryptocurrency_action(1.0) == "Do nothing"
