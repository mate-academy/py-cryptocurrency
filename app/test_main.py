from unittest import TestCase, mock

from app.main import cryptocurrency_action


class TestCryptocurrencyAction(TestCase):
    @mock.patch("app.main.get_exchange_rate_prediction", return_value=94)
    def test_cryptocurrency_action_rate_is_lower_than_current(
            self,
            mock_exchange_rate: int
    ) -> None:

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Sell all your cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction", return_value=106)
    def test_cryptocurrency_action_rate_is_higher_than_current(
            self,
            mock_exchange_rate: int
    ) -> None:

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Buy more cryptocurrency")

    @mock.patch("app.main.get_exchange_rate_prediction", return_value=100)
    def test_cryptocurrency_action_rate_is_stable(
            self,
            mock_exchange_rate: int
    ) -> None:

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction", return_value=105)
    def test_cryptocurrency_action_rate_is_a_little_higher(
            self,
            mock_exchange_rate: int
    ) -> None:

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")

    @mock.patch("app.main.get_exchange_rate_prediction", return_value=95)
    def test_cryptocurrency_action_rate_is_a_little_lower(
            self,
            mock_exchange_rate: int
    ) -> None:

        result = cryptocurrency_action(100)
        self.assertEqual(result, "Do nothing")
