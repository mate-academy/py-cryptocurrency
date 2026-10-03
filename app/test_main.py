from unittest.mock import MagicMock, patch

from app.main import cryptocurrency_action


@patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more_cryptocurrency(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 110

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all_cryptocurrency(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 90

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_increase_is_less_than_five_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 104

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_decrease_is_less_than_five_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 96

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_increase_is_exactly_five_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 105

    assert cryptocurrency_action(100) == "Do nothing"


@patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_when_decrease_is_exactly_five_percent(
    mock_prediction: MagicMock,
) -> None:
    mock_prediction.return_value = 95

    assert cryptocurrency_action(100) == "Do nothing"
