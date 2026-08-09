from unittest import mock
from app import main


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_prediction: mock.MagicMock
) -> None:

    mock_prediction.return_value = 106.0
    actual_result = main.cryptocurrency_action(100.0)
    assert actual_result == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_your_cryptocurrency(
        mock_prediction: mock.MagicMock
) -> None:

    mock_prediction.return_value = 94.0
    actual_result = main.cryptocurrency_action(100.0)
    assert actual_result == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_upper_boundary(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 105.0
    actual_result = main.cryptocurrency_action(100.0)
    assert actual_result == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_lower_boundary(
        mock_prediction: mock.MagicMock
) -> None:
    mock_prediction.return_value = 95.0
    actual_result = main.cryptocurrency_action(100.0)
    assert actual_result == "Do nothing"
