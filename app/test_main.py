from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_buy_more(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 110.0
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_sell_all(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 90.0
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_at_upper_boundary(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 105.0
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_at_lower_boundary(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 95.0
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_should_do_nothing_if_rate_stable(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 100.0
    assert cryptocurrency_action(100) == "Do nothing"
