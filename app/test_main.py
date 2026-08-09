from unittest.mock import patch, MagicMock
import app.main as main


@patch("app.main.random.choice")
@patch("app.main.random.random")
def test_buy_more(mock_random: MagicMock, mock_choice: MagicMock) -> None:
    mock_choice.return_value = "increase"
    mock_random.return_value = 0.5
    assert main.cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.random.choice")
@patch("app.main.random.random")
def test_sell_all(mock_random: MagicMock, mock_choice: MagicMock) -> None:
    mock_choice.return_value = "decrease"
    mock_random.return_value = 0.5
    assert main.cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.random.choice")
@patch("app.main.random.random")
def test_do_nothing(mock_random: MagicMock, mock_choice: MagicMock) -> None:
    mock_choice.return_value = "decrease"
    mock_random.return_value = 0.95
    assert main.cryptocurrency_action(100) == "Do nothing"


@patch("app.main.random.choice")
@patch("app.main.random.random")
def test_exactly_105_do_nothing(
    mock_random: MagicMock, mock_choice: MagicMock
) -> None:
    mock_choice.return_value = "increase"
    mock_random.return_value = 100 / 105
    assert main.cryptocurrency_action(100) == "Do nothing"


@patch("app.main.random.choice")
@patch("app.main.random.random")
def test_exactly_095_do_nothing(
    mock_random: MagicMock, mock_choice: MagicMock
) -> None:
    mock_choice.return_value = "decrease"
    mock_random.return_value = 0.95
    assert main.cryptocurrency_action(100) == "Do nothing"
