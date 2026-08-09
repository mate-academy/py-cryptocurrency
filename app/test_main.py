import unittest
from unittest import mock
from unittest.mock import MagicMock

from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
class TestCryptocurrencyAction(unittest.TestCase):
    def test_predicted_rate_is_more_than_5_percent_higher_than_current(
            self,
            mocked_exchange_rate_prediction: MagicMock,
    ) -> None:
        mocked_exchange_rate_prediction.return_value = 6
        current_rate = 5.7
        assert cryptocurrency_action(current_rate) == "Buy more cryptocurrency"

    def test_predicted_rate_is_more_than_5_percent_lower_than_current(
            self,
            mocked_exchange_rate_prediction: MagicMock,
    ) -> None:
        mocked_exchange_rate_prediction.return_value = 2
        current_rate = 2.2
        assert (cryptocurrency_action(current_rate)
                == "Sell all your cryptocurrency")

    def test_predicted_rate_is_out_of_specified_cases(
            self,
            mocked_exchange_rate_prediction: MagicMock,
    ) -> None:
        mocked_exchange_rate_prediction.return_value = 98
        current_rate = 100
        assert cryptocurrency_action(current_rate) == "Do nothing"

    def test_rate_is_exactly_5_percent_lower(
            self,
            mocked_exchange_rate_prediction: MagicMock,
    ) -> None:
        mocked_exchange_rate_prediction.return_value = 95
        current_rate = 100
        assert cryptocurrency_action(current_rate) == "Do nothing"

    def test_rate_is_exactly_5_percent_higher(
            self,
            mocked_exchange_rate_prediction: MagicMock,
    ) -> None:
        mocked_exchange_rate_prediction.return_value = 105
        current_rate = 100
        assert cryptocurrency_action(current_rate) == "Do nothing"
