import unittest
from unittest.mock import patch
from app.main import cryptocurrency_action


class TestCryptocurrencyAction(unittest.TestCase):
    def test_buy_more_cryptocurrency(self) -> None:
        """Test when predicted rate is more than 5% > than current rate."""
        current_rate = 100.0
        predicted_rate = 110.0  # 10% increase
        with patch("app.main.get_exchange_rate_prediction",
                   return_value=predicted_rate) as mock_prediction:
            result = cryptocurrency_action(current_rate)
            self.assertEqual(result, "Buy more cryptocurrency")
            mock_prediction.assert_called_once_with(current_rate)

    def test_sell_all_cryptocurrency(self) -> None:
        """Test when predicted rate is more than 5% < than current rate."""
        current_rate = 100.0
        predicted_rate = 90.0  # 10% decrease
        with patch("app.main.get_exchange_rate_prediction",
                   return_value=predicted_rate) as mock_prediction:
            result = cryptocurrency_action(current_rate)
            self.assertEqual(result, "Sell all your cryptocurrency")
            mock_prediction.assert_called_once_with(current_rate)

    def test_do_nothing_small_increase(self) -> None:
        """Test when predicted rate increases but less than 5%."""
        current_rate = 100.0
        predicted_rate = 105.0  # 4% increase
        with patch("app.main.get_exchange_rate_prediction",
                   return_value=predicted_rate) as mock_prediction:
            result = cryptocurrency_action(current_rate)
            self.assertEqual(result, "Do nothing")
            mock_prediction.assert_called_once_with(current_rate)

    def test_do_nothing_small_decrease(self) -> None:
        """Test when predicted rate decreases but less than 5%."""
        current_rate = 100.0
        predicted_rate = 95.0  # 4% decrease
        with patch("app.main.get_exchange_rate_prediction",
                   return_value=predicted_rate) as mock_prediction:
            result = cryptocurrency_action(current_rate)
            self.assertEqual(result, "Do nothing")
            mock_prediction.assert_called_once_with(current_rate)

    def test_do_nothing_no_change(self) -> None:
        """Test when predicted rate is the same as current rate."""
        current_rate = 100.0
        predicted_rate = 100.0  # No change
        with patch("app.main.get_exchange_rate_prediction",
                   return_value=predicted_rate) as mock_prediction:
            result = cryptocurrency_action(current_rate)
            self.assertEqual(result, "Do nothing")
            mock_prediction.assert_called_once_with(current_rate)


if __name__ == "__main__":
    unittest.main()
