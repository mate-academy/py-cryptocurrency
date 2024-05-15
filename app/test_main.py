from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.94 * 100
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.10 * 100
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_1(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1 * 100
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_2(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 0.95 * 100
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_3(
        mock_get_exchange_rate_prediction: mock.MagicMock
) -> None:
    mock_get_exchange_rate_prediction.return_value = 1.05 * 100
    assert cryptocurrency_action(100) == "Do nothing"
