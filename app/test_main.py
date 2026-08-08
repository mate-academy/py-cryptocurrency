import pytest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency(self,
                                     mock_get_exchange_rate_prediction:
                                     int) -> None:
        current_rate = 100
        predicted_rate = 105.1
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency(self,
                                     mock_get_exchange_rate_prediction:
                                     int) -> None:
        current_rate = 100
        predicted_rate = 94.9
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert (cryptocurrency_action(current_rate)
                == "Sell all your cryptocurrency")

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing(self,
                        mock_get_exchange_rate_prediction:
                        int) -> None:
        current_rate = 100
        predicted_rate = 100.04
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_equal(self,
                              mock_get_exchange_rate_prediction:
                              int) -> None:
        current_rate = 100
        predicted_rate = 100
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_lower(self,
                              mock_get_exchange_rate_prediction:
                              int) -> None:
        current_rate = 100
        predicted_rate = 99.99
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_95_percent(self,
                                   mock_get_exchange_rate_prediction:
                                   int) -> None:
        current_rate = 100
        predicted_rate = 95
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == "Do nothing"

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_105_percent(self,
                                    mock_get_exchange_rate_prediction:
                                    int) -> None:
        current_rate = 100
        predicted_rate = 105
        mock_get_exchange_rate_prediction.return_value = predicted_rate
        assert cryptocurrency_action(current_rate) == "Do nothing"


if __name__ == "__main__":
    pytest.main()
