import unittest
from unittest.mock import patch, MagicMock


from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
class TestCryptocurrency(unittest.TestCase):
    def test_cryptocurrency_action(self, mock_prediction: MagicMock) -> None:
        test_cases = [
            ("is_rising", 106, "Buy more cryptocurrency"),
            ("is_falling", 94, "Sell all your cryptocurrency"),
            ("is_stable", 100, "Do nothing"),
            ("is_stable", 105, "Do nothing"),
            ("is_stable", 95, "Do nothing")
        ]
        for action, rate, it_means in test_cases:
            with self.subTest(action=action):
                mock_prediction.return_value = rate
                result = cryptocurrency_action(100)
                self.assertEqual(result, it_means)
