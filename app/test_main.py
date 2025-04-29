import pytest
from unittest.mock import patch, Mock
from app.main import cryptocurrency_action


@pytest.mark.parametrize(
    "choice_value, random_value, expected_result",
    [
        ("increase", 0.8, "Buy more cryptocurrency"),
        ("decrease", 0.9, "Sell all your cryptocurrency"),
        ("decrease", 0.95, "Do nothing"),
        ("increase", 0.9523809523809523, "Do nothing"),
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
