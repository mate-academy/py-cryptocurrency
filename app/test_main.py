from unittest.mock import patch
from app.main import cryptocurrency_action
from unittest.mock import MagicMock


class TestCryptocurrencyAction:
    """Test cases for cryptocurrency_action function."""

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency_above_threshold(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test buying when predicted rate is more than 5% higher."""
        current_rate = 100.0
        predicted_rate = 106.0  # 6% increase
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Buy more cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_buy_more_cryptocurrency_at_boundary(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test buying when predicted rate is exactly at 1.05 threshold."""
        current_rate = 100.0
        predicted_rate = 105.01  # Just above 5% increase
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Buy more cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency_below_threshold(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test selling when predicted rate is more than 5% lower."""
        current_rate = 100.0
        predicted_rate = 94.0  # 6% decrease
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Sell all your cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_sell_all_cryptocurrency_at_boundary(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test selling when predicted rate is just below 0.95 threshold."""
        current_rate = 100.0
        predicted_rate = 94.99  # Just below 5% decrease
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Sell all your cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_no_significant_change(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test doing nothing when predicted rate change is not significant."""
        current_rate = 100.0
        predicted_rate = 102.0  # 2% increase
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Do nothing"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_exactly_at_upper_boundary(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test doing nothing when predicted rate is exactly 5% higher."""
        current_rate = 100.0
        predicted_rate = 105.0  # Exactly 5% increase (ratio = 1.05)
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Do nothing"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_exactly_at_lower_boundary(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test doing nothing when predicted rate is exactly 5% lower."""
        current_rate = 100.0
        predicted_rate = 95.0  # Exactly 5% decrease (ratio = 0.95)
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Do nothing"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_do_nothing_same_rate(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test doing nothing when predicted rate equals current rate."""
        current_rate = 100.0
        predicted_rate = 100.0  # No change
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Do nothing"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_with_float_current_rate(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test with floating point current rate."""
        current_rate = 50.25
        predicted_rate = 53.0  # About 5.47% increase
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Buy more cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_with_integer_current_rate(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test with integer current rate."""
        current_rate = 200
        predicted_rate = 189.0  # 5.5% decrease
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Sell all your cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_high_predicted_rate(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test with significantly higher predicted rate."""
        current_rate = 10.0
        predicted_rate = 20.0  # 100% increase
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Buy more cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)

    @patch("app.main.get_exchange_rate_prediction")
    def test_very_low_predicted_rate(
        self,
        mock_prediction: MagicMock
    ) -> None:
        """Test with significantly lower predicted rate."""
        current_rate = 100.0
        predicted_rate = 50.0  # 50% decrease
        mock_prediction.return_value = predicted_rate

        result = cryptocurrency_action(current_rate)

        assert result == "Sell all your cryptocurrency"
        mock_prediction.assert_called_once_with(current_rate)
