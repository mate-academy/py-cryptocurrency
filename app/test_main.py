import pytest
from unittest.mock import patch

from app.main import cryptocurrency_action


@pytest.fixture
def current_rate():
    return 100.0


@pytest.mark.parametrize("predicted_rate, expected_action", [
    (106.0, "Buy more cryptocurrency"),    # >5% increase
    (90.0, "Sell all your cryptocurrency"),  # >5% decrease
    (102.0, "Do nothing"),                  # <5% change
    (95.0, "Do nothing"),                  # <5% change
    (105.0, "Do nothing"),                  # <5% change
])
def test_cryptocurrency_action(current_rate, predicted_rate, expected_action):
    with patch("app.main.get_exchange_rate_prediction", return_value=predicted_rate):
        assert cryptocurrency_action(current_rate) == expected_action

