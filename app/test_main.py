from unittest import mock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_buy_more_cryptocurrency(mock_prediction: mock.MagicMock) -> None:
    mock_prediction.return_value = 105.1
    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_sell_all_cryptocurrency(mock_prediction: mock.MagicMock) -> None:
    mock_prediction.return_value = 94.9
    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_upper_boundary(mock_prediction: mock.MagicMock) -> None:
    mock_prediction.return_value = 105
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_on_lower_boundary(mock_prediction: mock.MagicMock) -> None:
    mock_prediction.return_value = 95
    assert cryptocurrency_action(100) == "Do nothing"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_do_nothing_within_range(mock_prediction: mock.MagicMock) -> None:
    mock_prediction.return_value = 100
    assert cryptocurrency_action(100) == "Do nothing"
