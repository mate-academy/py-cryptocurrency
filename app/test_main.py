import pytest
from app.main import cryptocurrency_action


# Mock function
def mock_get_exchange_rate_prediction(exchange_rate):
    if exchange_rate == 100:
        return 110
    if exchange_rate == 200:
        return 180
    if exchange_rate == 300:
        return 310
    return exchange_rate


@pytest.mark.parametrize("current_rate, expected_action", [
    (100, "Buy more cryptocurrency"),
    (200, "Sell all your cryptocurrency"),
    (300, "Do nothing"),
])
def test_cryptocurrency_action(monkeypatch, current_rate, expected_action):
    monkeypatch.setattr('app.main.get_exchange_rate_prediction', mock_get_exchange_rate_prediction)
    assert cryptocurrency_action(current_rate) == expected_action
