import pytest
from app.main import cryptocurrency_action, get_exchange_rate_prediction
from _pytest.monkeypatch import MonkeyPatch


# Mocking get_exchange_rate_prediction function
@pytest.fixture
def mock_get_exchange_rate_prediction(monkeypatch: MonkeyPatch) -> None: # Noqa E501
    def mock_prediction(current_rate: float) -> float:
        # Replace this with your mocked prediction logic
        return current_rate + 0.06 * current_rate

    monkeypatch.setattr("app.get_exchange_rate_prediction", mock_prediction)


def test_cryptocurrency_action_buy_more(mock_get_exchange_rate_prediction: None) -> None: # Noqa E501
    current_rate = 100.0
    result = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell_all(mock_get_exchange_rate_prediction: None) -> None: # Noqa E501
    current_rate = 100.0

    # Mocking prediction to be 5% lower than the current rate
    def mock_prediction(current_rate: float) -> float:
        return current_rate - 0.05 * current_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing(mock_get_exchange_rate_prediction: None) -> None: # Noqa E501
    current_rate = 100.0

    # Mocking prediction to be within the 5% difference threshold
    def mock_prediction(current_rate: float) -> float:
        return current_rate + 0.03 * current_rate

    result = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
