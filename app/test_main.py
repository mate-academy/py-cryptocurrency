from unittest.mock import patch, MagicMock
import pytest
from app.main import cryptocurrency_action, get_exchange_rate_prediction


@pytest.mark.parametrize(
    "m_choice, m_random, result",
    [
        ("increase", 0.5, 200.0),
        ("decrease", 0.5, 50.0)
    ]
)
@patch("app.main.random.choice")
@patch("app.main.random.random")
def test_random_choice(
        mock_random: MagicMock,
        mock_choice: MagicMock,
        m_choice: str,
        m_random: int,
        result: float):
    mock_choice.return_value = m_choice
    mock_random.return_value = m_random
    assert get_exchange_rate_prediction(100) == result


@pytest.mark.parametrize(
    "prediction, current, result",
    [
        (110, 100, "Buy more cryptocurrency"),
        (90, 100, "Sell all your cryptocurrency"),
        (100, 100, "Do nothing"),
        (105, 100, "Do nothing"),
        (95, 100, "Do nothing")
    ]
)
@patch("app.main.get_exchange_rate_prediction")
def test_print_cryptocurrency(
        mock_exchange_rate: MagicMock,
        prediction: int,
        current: int,
        result: str):
    mock_exchange_rate.return_value = prediction
    assert cryptocurrency_action(current) == result
