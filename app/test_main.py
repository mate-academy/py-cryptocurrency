# write your code here
from unittest.mock import patch
from app.main import cryptocurrency_action  # noqa: F401

# -----------------------------
# Тест 1: predicted > current * 1.05 → Buy
# -----------------------------
@patch("app.main.get_exchange_rate_prediction")
def test_buy_more(mock_prediction: "unittest.mock.Mock") -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 106.0  # > 105
    result: str = cryptocurrency_action(current_rate)
    assert result == "Buy more cryptocurrency"


# -----------------------------
# Тест 2: predicted < current * 0.95 → Sell
# -----------------------------
@patch("app.main.get_exchange_rate_prediction")
def test_sell_all(mock_prediction: "unittest.mock.Mock") -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 94.0  # < 95
    result: str = cryptocurrency_action(current_rate)
    assert result == "Sell all your cryptocurrency"


# -----------------------------
# Тест 3: predicted в пределах ±5% → Do nothing
# -----------------------------
@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing(mock_prediction: "unittest.mock.Mock") -> None:
    current_rate: float = 100.0
    mock_prediction.return_value = 102.0  # между 95 и 105
    result: str = cryptocurrency_action(current_rate)
    assert result == "Do nothing"
