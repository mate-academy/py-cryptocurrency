from unittest import mock
from app.main import cryptocurrency_action


class TestCryptocurrencyAction:
    current_rate = 100

    def test_buy_more_when_prediction_higher(self) -> None:
        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=self.current_rate * 1.1,
        ) as mock_prediction:
            result = cryptocurrency_action(self.current_rate)
            assert result == "Buy more cryptocurrency"
            mock_prediction.assert_called_once_with(self.current_rate)

    def test_sell_all_when_prediction_lower(self) -> None:
        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=self.current_rate * 0.9,
        ) as mock_prediction:
            result = cryptocurrency_action(self.current_rate)
            assert result == "Sell all your cryptocurrency"
            mock_prediction.assert_called_once_with(self.current_rate)

    def test_do_nothing_when_prediction_higher_but_similar(self) -> None:
        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=self.current_rate * 1.05,
        ) as mock_prediction:
            result = cryptocurrency_action(self.current_rate)
            assert result == "Do nothing"
            mock_prediction.assert_called_once_with(self.current_rate)

    def test_do_nothing_when_prediction_lower_but_similar(self) -> None:
        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=self.current_rate * 0.95,
        ) as mock_prediction:
            result = cryptocurrency_action(self.current_rate)
            assert result == "Do nothing"
            mock_prediction.assert_called_once_with(self.current_rate)

    def test_when_prediction_inside_threshold(self) -> None:
        with mock.patch(
            "app.main.get_exchange_rate_prediction",
            return_value=self.current_rate * 1.03,
        ) as mock_prediction:
            result = cryptocurrency_action(self.current_rate)
            assert result == "Do nothing"
            mock_prediction.assert_called_once_with(self.current_rate)
