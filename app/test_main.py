from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 106

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 94

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_increases_by_five_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_rate_decreases_by_five_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_when_difference_is_less_than_five_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 103

    assert cryptocurrency_action(100) == "Do nothing"
