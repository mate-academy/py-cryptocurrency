import pytest
from unittest.mock import patch, Mock
from app.main import cryptocurrency_action

@pytest.mark.parametrize(
    "random_value, choice_value, expected_result",
    [
        (0.2, "increase", "Buy more cryptocurrency"),       # > 1.05
        (0.9, "decrease", "Sell all your cryptocurrency"),  # < 0.95
        (0.951, "decrease", "Do nothing"),                  # ≈ 0.95
        (1.049, "increase", "Do nothing"),                  # ≈ 1.05
    ]
)
@patch("app.main.random.random")
@patch("app.main.random.choice")
def test_cryptocurrency_action(mock_choice: Mock,
                               mock_random: Mock,
                               random_value: float,
                               choice_value: str,
                               expected_result: str) -> None:
    mock_random.return_value = random_value
    mock_choice.return_value = choice_value

    result = cryptocurrency_action(100)
    assert result == expected_result

    mock_choice.assert_called_once()
    mock_random.assert_called_once()
