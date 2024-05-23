from unittest import mock
from app.main import cryptocurrency_action, get_exchange_rate_prediction

def test_get_exchange_rate_prediction_increase():
    with (mock.patch("random.random") as mock_random,
          mock.patch("random.choice") as mock_choice):

        mock_random.return_value = 0.1
        mock_choice.return_value = "increase"

        assert get_exchange_rate_prediction(10) == 100


def test_get_exchange_rate_prediction_decrease():
    with (mock.patch("random.random") as mock_random,
          mock.patch("random.choice") as mock_choice):

        mock_random.return_value = 0.1
        mock_choice.return_value = "decrease"

        assert get_exchange_rate_prediction(10) == 1

